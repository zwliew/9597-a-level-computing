#!/usr/bin/env python3

def binary_search(arr, n):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < n:
            lo = mid + 1
        elif arr[mid] > n:
            hi = mid - 1
        else:
            return mid
    return -1

arr = [1, 2, 5, 99, 12032, 12931289429, 12931283921839232]
print(binary_search(arr, 99))
print(binary_search(arr, 12931283921839232))
print(binary_search(arr, 0))
