#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cjeffcoa
"""

import math


def basic():
    # =============================================================================
    #     +     for a + b
    #     -     for a - b
    #     /     for a / b
    #     *     for a * b
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    elif op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    elif op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    elif op == '/':
        if b == 0:
            return 'Error: Cannot be divided by 0'
        else:
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    else:
        return "Incorrect operator! Please select from the given options!"


def scientific():
    # =============================================================================
    #     ^     for a ^ b
    #     %     for a mod b
    #     r     for the bth root of a (a ^ (1/b))
    #     !     for a factorial
    #     sin   for sin(a) in radians
    #     cos   for cos(a) in radians
    #     tan   for tan(a) in radians
    #     ln    for ln(a) (log base e of a)
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "^, r, %, !, sin, cos, tan, ln" : ')

    if op in '^r%':
        a = int(input('Please type the first number: '))
        b = int(input('Please type the second number: '))
    elif op in '!sincostanln':
        a = int(input('Please type the number: '))

    # Your solution here

    # Binary Operations
    # Checks for Power signs
    if op == '^':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a**b)
    # Checks for r for root
    elif op == 'r':
        if b == 0:
            return 'Error: Cannot be divided by 0'
        # By powering a to (1/b) it actually allows a to be rooted by b
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a**(1/b))
    # Checks for % for modulus
    elif op == '%':
        if b == 0:
            return 'Error: Cannot be divided by 0'
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a%b)

    # Unary Operations
    # Checks for ! for factorial
    if op == '!':
        total = 1
        # Uses a for-loop to multiply all numbers from 1 to a
        for i in range(1,a+1):
            total = total  * i
        return str(a) + op + ' = ' + str(total)
    # Checks for sin
    elif op == 'sin':
        return 'sin(' + str(a) +') = ' + str(math.sin(a))
    # Checks for cos
    elif op == 'cos':
        return 'cos(' + str(a) +') = ' + str(math.cos(a))
    # Checks for tan
    elif op == 'tan':
        return 'tan(' + str(a) +') = ' + str(math.tan(a))
    # checks for ln
    elif op == 'ln':
        if b == 0:
            return 'Error: -Infinity'
        return 'ln(' + str(a) +') = ' + str(math.log(a))

def main():  # Wrapper function

    print("""Choose a calculator
    1. Basic Calculator
    2. Scientific Calculator""")
    choice = int(input('Please choose as 1 or 2: '))

    if choice == 1:
        print(basic())
    elif choice == 2:
        print(scientific())
    else:
        print('Invalid choice! Please select between 1 and 2:')


if __name__ == '__main__':
    main()
