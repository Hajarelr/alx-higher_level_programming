#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    m = a_dictionary.copy()
    for x, y in m.items():
        if value == y:
            a_dictionary.pop(x)
    return (a_dictionary)
