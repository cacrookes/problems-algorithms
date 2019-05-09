#!/usr/bin/env python3


def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    assert len(ints) > 0, 'The list cannot be empty.'
    min = ints[0]
    max = ints[0]
    for num in ints:
        if num < min:
            min = num
        if num > max:
            max = num

    return(min, max)


def run_tests():
    print(get_min_max_by_sorting([1, 2, 3, 4, 5]))
    # Expected output: (1, 5)
    # Tests a simple sorted list

    print(get_min_max_by_sorting([5]))
    # Expected output: (5, 5)
    # Tests the edge case of a single element array

    print(get_min_max_by_sorting([1, 1, 1, 1]))
    # Expected output: (1, 1)
    # Tests the case where all elements have the same value

    print(get_min_max_by_sorting([5, 4, 3, 2]))
    # Expected output: (2, 5)
    # Tests a simple list sorted in descending order

    print(get_min_max_by_sorting([-8, 0, 5492, 12, 3]))
    # Expected output: (-8, 5492)
    # Tests negative values


if __name__ == '__main__':
    run_tests()
