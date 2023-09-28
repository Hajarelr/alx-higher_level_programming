#!/usr/bin/python3
"""Defines a peak-finding algorithm"""
def find_peak(list_of_integers):
""" Finds the peak in a list of integers """
if list_of_integers == []:
return None
length = len(list_of_integers)
n = int(length / 2)
m = list_of_integers
if n - 1 < 0 and n + 1 >= length:
return m[n]
elif n - 1 < 0:
return m[n] if m[n] > m[n + 1] else m[n + 1]
elif n + 1 >= length:
return m[n] if m[n] > m[n - 1] else m[n - 1]
if m[n - 1] < m[n] > m[n + 1]:
return m[n]
if m[n + 1] > m[n - 1]:
return find_peak(m[n:])
return find_peak(m[:n])
