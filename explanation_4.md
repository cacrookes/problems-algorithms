# Dutch National Flag Problem

The script `problem_4.py` includes the function `sort_012(input_list)` which takes in an
unsorted array of numbers in the set {0, 1, 2}, and returns the array in sorted order. For
example, an input list of `[2, 1, 2, 2, 0, 0, 1]` would return `[0, 0, 1, 1, 2, 2, 2]`.

## Requirements

Python 2.7 or Python 3.x is needed to run this script.

## Program Design

- Runtime complexity: `O(n)`
- Space efficiency: `O(n)`

The project description says the problem should be solved using a single traversal. So 
the algorithm traverses the list in order a singe time. Thus it runs in `O(n)` time.

The output is built using three temporary arrays that are grown as the algorithm loops
through the input list. The lengths of the three arrays will total the length of the input 
array. These three arrays are joined together to create the final sorted array, which is
of size n. So the space efficiency of the algorithm is `3 * n + C`, where `C` is some
constant. In big O notation, this is `O(n)`.
