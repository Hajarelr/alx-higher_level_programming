#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = my_list[:]
    for m, i in enumerate(my_list):
        if i % 2 == 0:
            n[m] = True
        else:
            n[m] = False
            return (n)
