#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    total = meal_cost + tip + tax
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input("Meal Cost: "))

    tip_percent = int(input("Tip Percentage: "))

    tax_percent = int(input("Tax Percentage: "))

    solve(meal_cost, tip_percent, tax_percent)
