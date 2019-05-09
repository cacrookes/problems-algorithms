# Max and Min in an Unsorted Array

The script `problem_6.py` includes the function `get_min_max_by_sorting(ints)` which takes in an
unsorted array of length 1 or more and returns the min value and max value in the array as a tuple.
For example, if the input is `[0, -8, 343, 10]`, the output will be `(-8, 343)`.

## Requirements

Python 2.7 or Python 3.x is needed to run this script.

## Program Design

- Runtime complexity: `O(n)`
- Space efficiency: `O(n)`

The `get_min_max_by_sorting(ints)` function finds the min and max integers in the array by traversing
the array one time. Since the list is unsorted, each element in the array will need to be visited at 
least once, so traversing the array one time, visiting each element once, will be the fastest way
to find the min and max values in the array.

Since only one array is used, the space efficiency of the algorithm is `O(n)`.
