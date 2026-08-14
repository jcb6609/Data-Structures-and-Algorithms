import numpy as np
import sys

def main():
    A = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

    B = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

    n = (len(A) + len(B)) # n = 6
    print(matrices_sum(A, B, n))

def matrices_sum(A, B, n):
    C = np.empty((3, 3), dtype=int)
    cou1 = -1
    cou2 = 0
    for i in range(0, (n - 3), 1): # i=0 ; i=1 ; i=2
        for j in range(0, (n - 3), 1): # i=0 -> j=0,j=1,j=2 ; i=1 -> j=0,j=1,j=2 ; i=2 -> j=0,j=1,j=2
            # i=0, j=0 ; i=0, j=1 ; i=0, j=2
            if (i == 0): # row 0
                if (j == 0): # C[0, 0]
                    C[i, j] = (A[i, j] * B[i, j]) + (A[i, (j + 1)] * B[(i + 1), j]) + (A[i, (j + 2)] * B[(i + 2), j])
                elif (j == 1): # C[0, 1]
                    C[i, j] = (A[i, (j - 1)] * B[i, j]) + (A[i, j] * B[(i + 1), j]) + (A[i, (j + 1)] * B[(i + 2), j])
                elif (j == 2): # C[0, 2]
                    C[i, j] = (A[i, (j - 2)] * B[i, j]) + (A[i, (j - 1)] * B[(i + 1), j]) + (A[i, j] * B[(i + 2), j])
            # i=1, j=0 ; i=1, j=1 ; i=1, j=2
            elif (i == 1): # row 1
                if (j == 0): # C[1, 0]
                    C[i, j] = (A[i, j] * B[(i - 1), j]) + (A[i, (j + 1)] * B[i, j]) + (A[i, (j + 2)] * B[(i + 1), j])
                elif (j == 1): # C[1, 1]
                    C[i, j] = (A[i, (j - 1)] * B[(i - 1), j]) + (A[i, j] * B[i, j]) + (A[i, (j + 1)] * B[(i + 1), j])
                elif (j == 2): # C[1, 2]
                    C[i, j] = (A[i, (j - 2)] * B[(i - 1), j]) + (A[i, (j - 1)] * B[i, j]) + (A[i, j] * B[(i + 1), j])
            # i=2, j=0 ; i=2, j=1 ; i=2, j=2
            elif (i == 2): # row 2
                if (j == 0): # C[2, 0]
                    C[i, j] = (A[i, j] * B[(i - 2), j]) + (A[i, (j + 1)] * B[(i - 1), j]) + (A[i, (j + 2)] * B[i, j])
                elif (j == 1): # C[2, 1]
                    C[i, j] = (A[i, (j - 1)] * B[(i - 2), j]) + (A[i, j] * B[(i - 1), j]) + (A[i, (j + 1)] * B[i, j])
                elif (j == 2): # C[2, 2]
                    C[i, j] = (A[i, (j - 2)] * B[(i - 2), j]) + (A[i, (j - 1)] * B[(i - 1), j]) + (A[i, j] * B[i, j])
                

    return C

if __name__ == "__main__":
    main()