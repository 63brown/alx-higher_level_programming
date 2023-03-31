#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    lst = list_of_integers
    if lst == []:
        return None
    start, end = 0, len(lst) - 1

    while start < end:
        mid = start + (end - start) // 2

        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]
        if lst[mid - 1] > lst[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return (lst[start])
