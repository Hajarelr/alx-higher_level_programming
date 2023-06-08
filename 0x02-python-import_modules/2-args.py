#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = sys.argv
    m = len(n) - 1
    if m > 1:
        print("{} arguments:".format(m))
        for o in range(1, m + 1):
            print("{}: {}".format(o, n[o]))
    elif m == 0:
        print("{} arguments.".format(m))
    else:
        print("{} argument:".format(m))
        print("{}: {}".format(m, n[1]))
