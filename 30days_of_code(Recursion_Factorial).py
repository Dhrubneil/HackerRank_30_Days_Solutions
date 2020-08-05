#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    fact = 1
    if n > 0:
        if n == 0 or n == 1:
            fact = 1
        else:
            for i in range(1, n+1):
                fact = fact * i
    else:
        return "Factorial of negative numbers are not defined."
    return f"Factorial of {n} is : {fact}"
if __name__ == '__main__':
    

    n = int(input("Enter any natural number: "))

    print(factorial(n))
