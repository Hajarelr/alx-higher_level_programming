#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    n = len(argv)
    if n != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    op = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if argv[2] in op:
        m = int(argv[1])
        o = int(argv[3])
        p = op[argv[2]]
        q = p(m, o)
        print('{:d} {:s} {:d} = {:d}'.format(m, argv[2], o, q))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
