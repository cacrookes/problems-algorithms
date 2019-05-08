# Finding the Square Root of an Integer

The script `problem_1.py` includes the function `sqrt(number)` which takes in a 
positive integer value, including 0, and returns the floored integer square 
root of that number.

## Requirements

Python 3.6 or greater is needed to run this script.

## Program Design

- Runtime complexity: `O(log(n))`
- Space efficiency: `O(1)`

The `sqrt(number)` function finds the square root of the number in `O(log(n))` 
time by using a binary search.

Since the square root of a number, x,  must be between 0 and x inclusive, the 
algorithm first checks if the square root of x is x (as would be the case when 
`x < 4`). The algorithm proceeds to hone in on the square root in a binary 
fashion, by continually halving the potential number of possible integers the 
result could be.

This binary search method was chosen due to its fast `O(log(n))` time.

Three variables are used to store the bounds of the potential results, and 
the mid point between the boundaries. This results in a `O(1)` constant space 
efficiency.