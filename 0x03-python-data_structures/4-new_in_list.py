#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = my_list[:]
    if 0 <= idx < len(my_list):
        n[idx] = element
        return(n)
    return(my_list)
