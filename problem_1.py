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
            return root
        if root * root > number:
            ceiling = root
            root = (ceiling + floor)//2
        else:
            floor = root
            root = (ceiling + floor)//2

    return root


def original_test_cases():
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    # if this function is run, "Pass" should be printed 5 times.


def main():
    print(f'Square root of 9 is: {sqrt(9)}')
    # Expected output: Square root of 9 is: 3
    # This tests a standard case.

    print(f'Square root of 0 is: {sqrt(0)}')
    # Expected output: Square root of 0 is: 0
    # This tests the edge case where the input is 0.

    print(f'Square root of 1 is: {sqrt(1)}')
    # Expected output: Square root of 1 is: 1
    # This tests the edge case where the square root is
    # equal to the input number

    print(f'Square root of 27 is: {sqrt(5)}')
    # Expected output: Square root of 27 is: 2
    # This tests that the floor of a square root is
    # returned if the square root is not an integer.

    print(f'Square root of 98596 is: {sqrt(98596)}')
    # Expected output: Square root of 98596 is: 314
    # This tests large numbers.


if __name__ == '__main__':
    # uncomment the line below to run the original
    # test cases supplied by Udacity.
    # original_test_cases()
    main()
