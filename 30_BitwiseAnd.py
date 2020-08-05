#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())
    my_set = set()
    my_list = []
    my_k = []
    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        my_set = set(range(1, n+1))
        my_list.append(my_set)
        my_k.append(k)
        
    #print(my_set)

    '''my_len = len(my_set)
    my_list = list(my_set)
    print(my_list)
    print(my_list[1:my_len:1])'''
    
    for i in range(len(my_list)):
        test_list = list(my_list[i])
        k = my_k[i]
        max_res = []
        
        for j in range(len(test_list)):
            curr = test_list[j]
            slice_list = test_list[j+1:len(test_list):1]

            for ele in slice_list:
                res = curr & ele
                if res < k:
                   max_res.append(res)
        print(max(max_res))