import numpy as np

def main():
    # recall --> 1D Array (Vector): e.g. [1, 2, 3] --> a single array
    # recall --> 2D Array (Matrix): e.g. [[1, 2], [3, 4], [5, 6]] (3(rows)x2(columns)) --> An array containing 1D arrays
    # recall --> 3D Array (Cube): e.g. [[[1, 2]], [[3, 4]]] --> An array containing 2D arrays

    # A = 2D array:
    A = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
    # A = 2D array:
    B = np.array([[7, 8, 9],
                 [10, 11, 12],
                 [13, 14, 15]])

    # when using len() in a 2d array, we would get its number of rows
    n = (len(A) + len(B)) # 'n = 6' since 'len(A) = 2' (A rows) and 'len(B) = 2' (B rows)
    # we could also use the .shape property, which returns a tuple of the referenced array's size (rxc) as (r, c); e.g. A.shape = (3, 3)
    print(matrices_sum(A, B, n))

def matrices_sum(A, B, n):
    C = np.empty((3, 3), dtype=int) # use the empty() function from np 'np.empty()' to define an empty array by passing its size as a tuple argument, in this case (3, 3) as (3x3) size, and also specifyint the data type content for the matrix arrays as 'dtype=int' (being 'dtype=float64' as default); so then having 'np.empty((3, 3), dtype=int)' 
    # need to fix n for (n - 1) instead, so that range() only counts up to 3 loops (0,1,2) instead of 4 (0,1,2,3 --> out of bound i rows)
    for i in range(0, (n - 3), 1): # range(3) --> 0,1,2 (3 loops)

    # for i=0, j=0,1,2,...,n; for i=1, j=0,1,2,...,n; and so on.
         # need to fix n for (n - 1) instead, so that range() only counts up to 3 loops (0,1,2) instead of 4 (0,1,2,3 --> out of bound j columns)
        for j in range(0, (n - 3), 1): # range(3) --> 0,1,2, (3 loops)

            # i = row index, j = column index
            C[i, j] = A[i, j] + B[i, j]

    return C


if __name__ == "__main__":
    main()