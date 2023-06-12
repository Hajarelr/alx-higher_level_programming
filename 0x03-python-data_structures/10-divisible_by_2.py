#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l = my_list[:]
    for c, i in enumerate(my_list):
        if i % 2 == 0:
            l[c] = True
        else:
            l[c] = False
    return(l)
