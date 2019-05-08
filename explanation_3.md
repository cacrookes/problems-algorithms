# Rearrange Array Elements

The script `problem_3.py` includes the function `rearrange_digits(input_list)`
which takes in a list of single digit postive integers, and then returns two
numbers made up of the integers in the list such that the sum of the two 
returned numbers is the maximum sum possible. The length of the two numbers may
only differ by at most 1.

## Requirements

Python 2.7 or Python 3.x is needed to run this script.

## Program Design

- Runtime complexity: `O(n)`
- Space efficiency: `O(n)`

The `rearrange_digits(input_list)` algorithm traverses the input list 10 times.
Each traversal visits each item in the list once, for a runtime complexity of n.
So the runtime of the algorithm is `10 * n + C`, where `C` is some constant.
In big O notation, this can be simplified to `O(n)`.

The algorithm makes use of the fact that each number in the list is in the range 
of [0, 9]. So I know I can find each number in the list by traversing the list 
a constant number of times, which in this case is 10.

The algorithm uses a single list, so the space efficiency is `O(n)`.
