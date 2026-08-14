import numpy as np

def main():
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    B = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    n = len(A) + len(B) # n = 3 + 3 = 6

    print(matrices_sum(A, B, n))


def matrices_sum(A, B, n):
    C = np.empty((3, 3), dtype=int)
    for i in range(0, (n - 3), 1): # i=0, i=1, i=2
        for j in range(0, (n - 3), 1): # j=0, j=1, j=2
            C[i, j] = 0
            for k in range(0, (n - 3), 1): # k=0, k=1, k=2
                C[i, j] += A[i, k] * B[k, j]

    return C


if __name__ == "__main__":
    main()