import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        my_res = 0

        for i in range(1, n):
            for j in range(i+1, n+1):
                res = i & j

                if my_res < res < k:
                    my_res = res
                '''
                this condition should be checked othewise, hackerrank 
                raises '...Terminated due to timeout...' error.
                '''
                if my_res == k - 1:
                    break
        print(my_res)



'''
 maxab = 0

    for a in xrange(n-1, 1, -1):

        for b in xrange(n, a, -1):

            ab = a&b

            if ab < k and ab > maxab:
                maxab = ab

            if maxab == k-1:
                break

        if maxab == k-1:
            break

    print(maxab)
'''