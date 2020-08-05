#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter any number: "))
    
    if n in range(2, 21):
        for i in range(1, 11):
            print(f"{n} x {i} =", n*i)
    else:
        print("Do nothing.")