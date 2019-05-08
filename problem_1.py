#!/usr/bin/env python3


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    assert number >= 0, "Number must be 0 or a positive integer."

    floor = 0
    ceiling = number
    root = ceiling
    while floor < root:
        if root * root == number:
            print(f'Number: {number} Root: {root}')
            return root
        if root * root > number:
            ceiling = root
            root = (ceiling + floor)//2
        else:
            floor = root
            root = (ceiling + floor)//2

    print(f'Number: {number} Root: {root}')
    return root


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
