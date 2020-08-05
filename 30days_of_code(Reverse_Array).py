#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(arr)
    rarr = [ele for ele in reversed(arr)]
    print(rarr)
    for ele in rarr:
        print(ele,end=" ")
    print('')
    for i in range(0, len(arr)):
        a = len(arr)-i-1
        print(arr[a], end =" ")

        #print(a)