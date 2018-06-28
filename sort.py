#!/usr/bin/env python3

def bubble_sort(arr):
    end = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, end):
            if arr[i - 1] > arr[i]:
                swapped = True
                tmp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = tmp
        end -= 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp

def quick_sort(arr, lo, hi):
    if lo >= hi:
        return
    p = partition(arr, lo, hi)
    quick_sort(arr, lo, p)
    quick_sort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

arr = [5, 8, 1, 3, 0, 1, 10, 0]
print(arr)
bubble_sort(arr)
print(arr)

arr = [5, 8, 1, 3, 0, 1, 10, 0]
print(arr)
insertion_sort(arr)
print(arr)

arr = [5, 8, 1, 3, 0, 1, 10, 0]
print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
