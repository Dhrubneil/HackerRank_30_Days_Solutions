#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
nos = 0
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            nos += 1

print("Array is sorted in", nos, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[len(a)-1])