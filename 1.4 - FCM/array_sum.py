import numpy as np
import sys
# What is an array?
# --> data structure tht stores a collection of items typically in a contiguous block of memory. Thta means all itmes in an array have the same data type and they are stored in an specific order

def main():

    A = np.array([1, 2, 3, 4, 5]) # A is an array of size 5
    n = len(A) # n = 5
    print(sum(A, n))


# the sum() algorithm finds the sum of all the elements in an array
def sum(A, n):
    sum = 0
    """
    range(stop)              # stop (Req): the integer where the sequence ends. It is exclusive (the sequence stops before reaching this number)
    range(start, stop)       # start (Opt): the integer where the sequence begins (0 by default)
    range(start, stop, step) # step (Opt): the integer value determines that determines the increment between each number (1 by default)
    """
    # By default: 'for i in range(0, 5, 1):'
    # 'for i in range(5):' --> 0 1 2 3 4 --> 5 iterations from 0 to 4
    for i in range(n): # we could also do 'for i in range(len(A)):'
        sum += A[i]
    return sum


if __name__ == "__main__":
    main()