#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(arr)

    for i in range(len(arr)):
        print(arr[i])

    print(len(arr))

    print(len(arr[0]))
    
    max_sum = -63
    my_sum = 0

    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[0])-2):
            my_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + 
                                  arr[i+1][j+1] + 
                     arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]) 
            max_sum = max(max_sum, my_sum)

    print(max_sum)