#!/usr/bin/env python3

# Created by Jonathan Pasco-Arnone
# Created on November
# This program calculates the price of pizza

import math


def main():
    diameter_Str = input("What diameter of pizza would you like: ")
    diameter = int(diameter_Str)
    labor = 0.75
    rent = 1
    HST = 1.13
    subtotal = rent + labor + (diameter * 0.5)
    total = math.floor(subtotal * HST * 100)/100
    print("The cost of a {} inch pizza is: ${:.2f}".
          format(diameter_Str, total))


if __name__ == "__main__":
    main()
