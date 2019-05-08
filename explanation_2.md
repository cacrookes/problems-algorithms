# Search in a Rotated Sorted Array

The script `problem_2.py` includes the function `rotated_array_search(input_list, number)` which takes in a 
rotated sorted array and a number, and returns the index of that number in the array. If the number is not
found, `-1` is returned.

## Requirements

Python 2.7 or Python 3.x is needed to run this script.

## Program Design

- Runtime complexity: `O(log(n))`
- Space efficiency: `O(n)`

The `rotated_array_search(input_list, number)` function finds the indes of the number 
in the array in `O(log(n))` time by using two binary searchs.

First a binary search is used to find the pivot in the rotated array. Once the pivot
is known, we can establish a lower and upper bound on the possible indexes the number
may be found in. The algorithm proceeds to do a binary search within the slice of the 
array determined by these lower and upper bounds. 

By doing a constant number of binary searches, the algorithm completes in a fast `O(log(n))`
time. Since only one array is used, the space efficiency of the algorithm is `O(n)`.
