"""Lab 05 portfolio submission template (Exercise 1 code).

Submit this file, plus a separate .md or .txt file with your written
explanation, to Gradescope. Fill in the TODOs below - do not rename either
function, the autograder looks up `generate_table` by name.

What you need to do:
  1. Implement `gram_schmidt_qr`: the classical Gram-Schmidt QR
     factorisation, as covered in the lectures.
  2. Implement `generate_table`: build the eps/error1/error2/error3 table
     for eps = 10**-6, ..., 10**-16 using `gram_schmidt_qr`, and save it to
     "table.csv" in the working directory - the autograder looks for that
     exact filename, with a header row and columns named exactly
     eps, error1, error2, error3.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def A_func(eps):
    return np.array([[1, 1 + eps], [1 + eps, 1]], dtype=float)


def gram_schmidt_qr(A):
    """
    Compute the QR factorisation of a square matrix using the classical
    Gram-Schmidt process.

    Parameters
    ----------
    A : numpy.ndarray
        A square 2D NumPy array of shape ``(n, n)`` representing the input
        matrix.

    Returns
    -------
    Q : numpy.ndarray
        Orthonormal matrix of shape ``(n, n)`` where the columns form an
        orthonormal basis for the column space of A.
    R : numpy.ndarray
        Upper triangular matrix of shape ``(n, n)``.
    """
    n, m = A.shape
    if n != m:
        raise ValueError(f"the matrix A is not square, {A.shape=}")

    Q = np.empty_like(A)
    R = np.zeros_like(A)

    # TODO: fill in Q and R

    for j in range(n):
        # Start with a copy of the jth column of A
        # ex. [ 2, 5, 7 ] Produces - [ 2, 3, 1 ] for j = 0,
        #     [ 3, 6, 8 ]            [ 5, 6, 9 ] for j = 1 and 
        #     [ 1, 9 ,0 ]            [ 1, 9, 0 ] for j = 2 
        u = A[:, j].copy()

        # orthogonalise against the previous columns 
        # (remove bias towards a particular column, and its kept for the next subtraction on the next column)
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            u -= R[i, j] * Q[:, i]

        R[j, j] = np.linalg.norm(u)
        Q[:, j] = u/R[j, j]

    return Q, R


def generate_table():
    """
    Build the eps/error1/error2/error3 table for eps = 10**-6, ..., 10**-16
    using gram_schmidt_qr, and save it to "table.csv" (the autograder looks
    for this exact filename).
    """
    # TODO: build the table and save it, e.g.
    # import pandas as pd
    #
    # rows = []
    # for eps in [10**-j for j in range(6, 17)]:
    #     ...
    #     rows.append(
    #         {"eps": eps, "error1": error1, "error2": error2, "error3": error3}
    #     )
    # pd.DataFrame(rows).to_csv("table.csv", index=False)

    results = []
    error_range = [10**-j for j in range(6, 17)]
    for eps in error_range:

        A = A_func(eps)
        Q, R = gram_schmidt_qr(A)
        n = Q.shape[0]

        error1 = np.linalg.norm(A - Q @ R)
        error2 = np.linalg.norm(Q.transpose() @ Q - np.eye(n))
        error3 = np.linalg.norm(R - np.triu(R))


        results.append(
            { "eps":eps, "error1":error1, "error2":error2, "error3":error3 } 
        )
    pd.DataFrame(results).to_csv("table.csv", index=False)

    plt.xlabel("Margin of error")
    plt.ylabel("Accuracy")
    plt.title("Error of QR factorisation given different techniques")
    plt.plot(error_range,[ x["error1"] for x in results], label="error1")
    plt.plot(error_range,[ x["error2"] for x in results], label="error2")
    plt.plot(error_range,[ x["error3"] for x in results], label="error3", alpha=0.7)
    plt.yscale('log')
    plt.legend()
    dpi=300
    plt.savefig("errorplot.png",dpi=dpi)




if __name__ == "__main__":
    generate_table()
