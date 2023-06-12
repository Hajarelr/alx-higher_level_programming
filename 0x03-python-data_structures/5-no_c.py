#!/usr/bin/python3
def no_c(my_string):
    n = ""
    for m in my_string:
        if (m != 'c') and (m != 'C'):
            n += m
    return (n)
