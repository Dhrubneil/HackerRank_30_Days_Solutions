#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input("Enter any number: "))
    
    if N % 2 != 0:
        print(f"{N} is Weird")
    else:
        if N in range(2,6):
            print(f"{N} is Not Weird")
        elif N in range(6,21):
            print(f"{N} is Weird")
        else:
            print(f"{N} is Not Weird")