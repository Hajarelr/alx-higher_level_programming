#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = []
    for m in range(0, list_length):
        try:
            o = my_list_1[m] / my_list_2[m]
        except TypeError:
            print("wrong type")
            o = 0
        except ZeroDivisionError:
            print("division by 0")
            o = 0
        except IndexError:
            print("out of range")
            o = 0
        finally:
            n.append(o)
    return (n)
