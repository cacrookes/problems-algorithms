#!/usr/bin/env python3

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    assert len(input_list) > 1, "The input list must have a length of at least 2."
    level = 1
    x = 0
    y = 0
    last_add = 'y'
    for i in range(10):
        for num in input_list:
            if num == i:
                if last_add == 'y':
                    x += i * level
                    last_add = 'x'
                else:
                    y += i * level
                    last_add = 'y'
                    level *= 10

    return(x, y)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


def main():
    # original Udacity supplied test cases
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    # Expected output: Pass
    # Tests the algorith works with a sorted list with an odd number of items.
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    # Expected output: Pass
    # Tests the algorithm works with an unsorted list with an even number of
    # items.
    print(rearrange_digits([1, 2]))
    # Expected output: (1, 2)
    # Tests the edge case where there are only 2 items in the list. The
    # function asserts there must be at least 2 items in the list.

    print(rearrange_digits([1, 9, 1]))
    # expected output: (91, 1)
    # Tests the edge case of the smallest odd numbered length list works. It
    # also tests the algoritm works with duplicate values among the numbers
    # in the list.

    print(rearrange_digits([1, 0, 0, 3, 9, 9, 9, 3, 1]))
    # Expected output: (99310, 9310)
    # Tests the algorithm works with 0's, and with multiple duplicated values.


if __name__ == '__main__':
    main()
