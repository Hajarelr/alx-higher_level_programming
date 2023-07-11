#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    v = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for n in sys.stdin:
            if c == 10:
                print_stats(size, status_codes)
                c = 1
            else:
                c += 1

            n = n.split()

            try:
                size += int(n[-1])
            except (IndexError, ValueError):
                pass

            try:
                if n[-2] in v:
                    if status_codes.get(n[-2], -1) == -1:
                        status_codes[n[-2]] = 1
                    else:
                        status_codes[n[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
