#!/usr/bin/python3
def add_arg(argv):
    i = len(argv) - 1
    if i == 0:
        print("{:d}".format(i))
        return
    else:
        m = 1
        n = 0
        while m <= i:
            n += int(argv[m])
            m += 1
        print("{:d}".format(n))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
