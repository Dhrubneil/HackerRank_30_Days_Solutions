#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input("Enter a decimal number: "))

    div = n
    binary = ""
    
    while div > 0:
        qtn = int(div / 2)
        rem = str(div % 2)
        div = qtn
        binary += rem 
    
    rev = [ele for ele in reversed(binary)]

    string = ""
    for ele in rev:
        string += ele
    print(f"The equivalent binary number of {n} is '{string}'")
    
    print("The maximum number of consecustive 1's in", string, "is", max(map(len, string.split('0'))))
    
    split_list = string.split('0')
    print(f"Splitted List : {split_list}")

    ele_length = list(map(len, split_list))
    print(f"Length of each element in the splitted list : {ele_length}")

    max_length = max(ele_length)
    print(f"The max length of element in the splitted list: {max_length}")


