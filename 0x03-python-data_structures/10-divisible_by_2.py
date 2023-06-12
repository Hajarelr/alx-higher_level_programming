#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_i = my_list[:]
    for c, i in enumerate(my_list):
        if i % 2 == 0:
            list_i[c] = True
        else:
            list_i[c] = False
    return(list_i)
