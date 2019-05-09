#!/usr/bin/env python3


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_list = []
    one_list = []
    two_list = []
    for num in input_list:
        if num == 0:
            zero_list.append(0)
        elif num == 1:
            one_list.append(1)
        else:
            two_list.append(2)

    return zero_list + one_list + two_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


def run_tests():
    # Original test cases supplied by Udacity
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    # Expected output: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
    # This tests the case of an unsorted list starting with 0.
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    # Expected output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # This tests a larger unsorted list starting with 2.
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    # Expected output: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    # This tests if the algorithm works on a list that is already sorted.

    # My Own Tests
    test_function([0])
    # Expected output: [0]
    # This tests the edge case of there only being one element in the array.

    test_function([1])
    # Expected output: [1]
    # This will test if the algorithm works with a single element array containing a 1

    test_function([2])
    # Expected output: [2]
    # This will test if the algorithm works with a single element array containing a 2

    test_function([2, 2, 2, 1, 0, 0])
    # Expected output: [0, 0, 1, 2, 2, 2]
    # This tests how the algorith handles an array that is orignally sorted in descending order


if __name__ == '__main__':
    run_tests()
