---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
# Theoretical Foundations of Computer Science II COMP2870

**School of Computer Science, University of Leeds**

## Lab 03: Linear systems of equations
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
On-time submission date: **Friday 6 November 2026, 2:00pm**

Final completion date: **Friday 22 January 2027, 2:00pm**
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
- You are expected to submit a serious attempt for each portfolio task by the on-time submission date. Serious attempts should include attempts at every question and should show some relevant knowledge, understanding or engagement. This will allow you to act on feedback and keep up-to-date.
- Late submissions and resubmissions will be accepted up until the final completion date, but no submissions or resubmissions of Semester 1 portfolio tasks will be accepted after this time.
- You must pass all of the Semester 1 portfolio tasks.
- Failure to pass all of the Semester 1 portfolio tasks will result in failing the portfolio component and therefore the module overall.
- To pass this portfolio task, your submission must clearly demonstrate that you have achieved the learning outcome(s) listed below. Your work should be complete and substantially correct.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
This worksheet contains a combination of *formative activities* (which contribute towards your learning) and *summative activities* (which you will complete and submit to be assessed as part of your portfolio).

Every exercise in a box marked **Portfolio exercise** is a summative exercise and must be submitted as part of your portfolio. You should use Gradescope to submit portfolio activities.

Activities marked $\color{blue}{(\ast)}$ are advanced, and may take some time to complete.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
**Expectations:**

1. **Timeliness:** You should complete all of the activities in the order provided and submit your portfolio evidence to Gradescope before the completion date.
2. **Presentation:** You should present all of your work clearly and concisely following any additional guidance provided by the module staff in the module handbook.
3. **Integrity:** You are responsible for ensuring that the evidence you submit as part of your portfolio is entirely your own work. You can find out more about academic integrity on the [Skills@library website](https://library.leeds.ac.uk/info/1401/academic-skills/46/academic-integrity-and-plagiarism). All work you submit for assessment is subject to the academic integrity policy. Failure to comply with these requirements may be considered academic misconduct under University regulations.

**Feedback:** Feedback on formative activities will be provided via tutorials. Feedback on evidence submitted as part of the portfolio will be available on Gradescope.

**Support opportunities:** Support with the activity sheet is available in the Lab classes and tutorials. Individual support is available via the online booking system.

**Statement on the Use of Generative AI:**
The aim of this task is for you to develop and demonstrate the specific skills and knowledge covered in the taught sessions. We want you to independently develop and demonstrate your understanding, critical thinking and other fundamental skills that will be required throughout your programme. Reliance on GenAI could **prevent you from achieving** the intended learning outcomes and may **impede your skill development**.

You are permitted to use dictionaries, thesauri, spelling and grammar-checking software to help identify and correct spelling mistakes and grammatical errors (even if they are powered by Gen AI).

**Expected time for completion:** 1-2 hours
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
## Coursework summary

This lab covers material on how to solve systems of linear equations.

## Learning outcomes

On completion of this activity sheet you will have demonstrated that you can:

- Write code to solve systems of linear equations using direct methods.
- Accurately measure the run time of different implementations to test algorithm performance.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
## How to access the lab

You can access the lab worksheet directly through [minerva](https://minerva.leeds.ac.uk/), [github](https://github.com/COMP2870-2627/linear-algebra-student-labs) or using Noteable (accessible via Minerva - see `README.md` for detailed instructions).

These lab worksheets are written using ['Jupyter Notebooks'](https://jupyter.org/). Many, many tutorials and guides are [available online](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
First some helper code for generating good matrices for LU factorisation tests. 
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
import numpy as np
from scipy.sparse import diags


def generate_safe_system(n):
    """
    Generate a linear system A x = b where A is weakly diagonally dominant,
    ensuring LU factorization without pivoting will work.

    Parameters:
        n (int): Size of the system (n x n)

    Returns:
        A (ndarray): n x n weakly diagonally dominant matrix
        b (ndarray): RHS vector
        x_true (ndarray): The true solution vector
    """

    k = [np.ones(n - 1), -2 * np.ones(n), np.ones(n - 1)]
    offset = [-1, 0, 1]
    A = diags(k, offset).toarray()

    # Solution is always all ones
    x_true = np.ones((n, 1))

    # Compute b = A @ x_true
    b = A @ x_true

    return A, b, x_true
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
## Exercise 1: LU factorisation

<div class="alert alert-block alert-danger">
<b>Portfolio exercise</b>
You should submit a single Python file containing all required functions and outputs. The autograder will import and execute functions directly from this file. You should include:

1. Your code for `lu_factorisation`. This must be your own implementation -
   calling a library routine such as `scipy.linalg.lu`/`lu_factor` (or any
   other pre-built decomposition) instead of writing the algorithm yourself
   will be flagged and scored as zero, since that's the skill this exercise
   assesses. You must not import `scipy.linalg` or `sympy`.
2. The unmodified `row_add`/`gaussian_elimination` code from this sheet.
3. Your `runtime_comparison()` function (see Part 5 below). It must save its
   plot to a file named `plot.png` in the working directory - this is the
   exact file the autograder looks for.
4. Your submission should print the value returned by `determinant(A_large)` when run.

You may wish to use the template file `lab03_submission_template.py`.
</div>

Throughout this question, you may assume that all pivots are non-zero (that is the matrix admits an LU factorisation without pivoting).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
1. Derive the LU factorisation algorithm for an $n \times n$ matrix $A$ as described [in the
notes](https://comp2870-2627.github.io/linear-algebra-notes/src/lec04.html#sec-LU-factorisation).

    1. First work through the example calculation for a $3 \times 3$ matrix.
    2. Next, recall the definition of upper and lower triangular matrices that:
       $$
       L_{ij} = 0 \quad\text{if}\quad i<j \quad\text{and}\quad
       U_{ij} = 0 \quad\text{if}\quad i>j.
       $$
    3. We want to compute $A = LU$. This means that
       $$
       A_{ij} = \sum_{k=1}^n L_{ik} U_{kj}.
       $$
       Use the fact that $L$ is lower triangular and $U$ is upper triangular to write
       $$
       A_{ij} = \sum_{k=1}^{\text{??}} L_{ik} U_{kj},
       $$
       where you need to find an expression in terms of $i$ and $j$ to replace $\text{??}$.
    4. Use your expression for $A_{ij}$ (from 3.) for $i \le j$ to determine an expression for $U_{ij}$ (using $L_{ii} = 1$). *Hint*: Separate the final term from the rest of the sum first.
    5. Use your expression for $A_{ij}$ (from 3.) for $i > j$ to determine an expression for $L_{ij}$. *Hint*: Separate the final term from the rest of the sum first.
    6. Work out the correct order to use these expressions (from 4. and 5.) so that all terms on the right-hand side have already been calculated.

*Hint*: It might help to work out these calculations on the $3 \times 3$ example to help you work out the general $n$ case.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
2. Implement the algorithm for LU factorisation as described above.
You should implement a Python function which accepts an $n \times n$
matrix $A$ represented as a numpy array and returns one lower triangular
matrix $L$ and one upper triangular matrix $U$ with $A = LU$.

    Here is some starter code:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["portfolio"]
def lu_factorisation(A):
    """
    Compute the LU factorisation of a square matrix A.

    The function decomposes a square matrix ``A`` into the product of a lower
    triangular matrix ``L`` and an upper triangular matrix ``U`` such that:

    .. math::
        A = L U

    where ``L`` has unit diagonal elements and ``U`` is upper triangular.

    Parameters
    ----------
    A : numpy.ndarray
        A 2D NumPy array of shape ``(n, n)`` representing the square matrix to
        factorise.

    Returns
    -------
    L : numpy.ndarray
        A lower triangular matrix with shape ``(n, n)`` and unit diagonal.
    U : numpy.ndarray
        An upper triangular matrix with shape ``(n, n)``.
    """
    n, m = A.shape
    if n != m:
        raise ValueError(f"Matrix A is not square {A.shape=}")

    # construct arrays of zeros with dtype float
    L, U = np.zeros_like(A, dtype=float), np.zeros_like(A, dtype=float)
    
    for j in range(n):
        L[j, j] = 1
        for i in range(j+1):
            adder = 0
            for k in range(i):
                adder += L[i,k] * U[k,j]
                
            U[i, j] = A[i, j] - adder
       
        for i in range(j+1, n):
            adder = 0
            for k in range(j):
                adder += L[i,k] * U[k,j]
            L[i, j] = (A[i, j] - adder)/U[j, j]


    
    return L, U
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
3. Test your solution on the matrix $A$:
   $$
   A = \begin{pmatrix}
   4 & 2 & 0 \\ 2 & 3 & 1 \\ 0 & 1 & 2.5
   \end{pmatrix}.
   $$
   First compute the LU factorisation by hand, showing all intermediate calculations, and then verify that $A = L U$.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["portfolio"]
A = np.array([[4,2,0],[2,3,1],[0,1,2.5]])
L, U = lu_factorisation(A)

print(L)
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
4. Consider the large matrix given by:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["portfolio"]
A_large, b_large, x_large = generate_safe_system(100)
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
We can use the LU factorisation as another way to compute the determinant of a matrix.
We can use the fact that we can easily compute the determinant of a triangular matrix and that $\det(XY) = \det(X) \det(Y)$.

Use the following code to determine the determinant of `A_large`:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["portfolio"]
def determinant(A):
    n = A.shape[0]
    L, U = lu_factorisation(A)

    det_L = 1.0
    det_U = 1.0

    for i in range(n):
        det_L *= L[i, i]
        det_U *= U[i, i]

    return det_L * det_U
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
5. Compare the runtime of your LU factorisation implementation with that of Gaussian elimination.

    Implement a function `runtime_comparison()` that runs this comparison end to end: it should time your `lu_factorisation` against `gaussian_elimination` across a range of matrix sizes, produce a log-log plot of the two.
   The plot should contain both timing curves on the same axes, together with axis labels and a legend.
   Save the plot to `"plot.png"` (via `plt.savefig("plot.png")`) - the autograder calls this function directly and looks for that exact file, so the filename is not optional.

    Use the following code as a starter (all necessary functions are listed given in the template file):

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["portfolio"]
def row_add(A, b, p, k, q):
    """
    Perform an in-place row addition operation on a linear system.

    This function applies the elementary row operation:

    ``row_p ← row_p + k * row_q``

    where `row_p` and `row_q` are rows in the coefficient matrix `A` and the
    right-hand side vector `b`. It updates the entries of `A` and `b`
    **in place**, directly modifying the original data.

    Parameters
    ----------
    A : numpy.ndarray
        A 2D NumPy array of shape ``(n, n)`` representing the coefficient matrix
        of the linear system.
    b : numpy.ndarray
        A 2D NumPy array of shape ``(n, 1)`` representing the right-hand side
        vector of the system.
    p : int
        The index of the row to be updated (destination row). Must satisfy
        ``0 <= p < n``.
    k : float
        The scalar multiplier applied to `row_q` before adding it to `row_p`.
    q : int
        The index of the source row to be scaled and added. Must satisfy
        ``0 <= q < n``.
    """
    n = A.shape[0]

    # Perform the row operation
    for j in range(n):
        A[p, j] = A[p, j] + k * A[q, j]

    # Update the corresponding value in b
    b[p, 0] = b[p, 0] + k * b[q, 0]


def gaussian_elimination(A, b):
    """
    Perform Gaussian elimination to reduce a linear system to upper triangular
    form.

    This function performs **forward elimination** to transform the coefficient
    matrix `A` into an upper triangular matrix, while applying the same
    operations to the right-hand side vector `b`. This is the first step in
    solving a linear system of equations of the form ``Ax = b`` using Gaussian
    elimination.

    Parameters
    ----------
    A : numpy.ndarray
        A 2D NumPy array of shape ``(n, n)`` representing the coefficient matrix
        of the system.
    b : numpy.ndarray
        A 2D NumPy array of shape ``(n, 1)`` representing the right-hand side
        vector.

    Returns
    -------
    None
        This function modifies `A` and `b` **in place** and does not return
        anything.
    """
    # find shape of system
    n = A.shape[0]

    # perform forward elimination
    for i in range(n - 1):
        # eliminate column i
        for j in range(i + 1, n):
            # row j
            factor = A[j, i] / A[i, i]
            row_add(A, b, j, -factor, i)
```

```python editable=true slideshow={"slide_type": ""} tags=["portfolio"]
def runtime_comparison():
    """
    Time lu_factorisation against gaussian_elimination across a range of
    matrix sizes, produce a log-log plot comparing the two, and save it
    to "plot.png" (the autograder looks for this exact filename).
    """


    matrix_sizes = [2,3,4,8,16,32,64,128,256]
    results_lu = []
    results_ge = []

    for size in matrix_sizes:

        A_lu, _, _ = generate_safe_system(size)
        A_ge, b, x = generate_safe_system(size)

        start_time = time.perf_counter()
        lu_factorisation(A_lu)
        end_time = time.perf_counter()
        total_time_lu = (end_time - start_time)
        results_lu.append(total_time_lu)

        start_time = time.perf_counter()
        gaussian_elimination(A_ge, b)
        end_time = time.perf_counter()
        total_time_ge = (end_time - start_time)
        results_ge.append(total_time_ge)
            
    plt.xlabel("Matrix Sizes (n)")
    plt.ylabel("Runtime (s)")
    plt.title("Gaussian Elimination vs. LU Factorisation")
    plt.loglog(matrix_sizes, results_lu, label="LU Factorisation")
    plt.loglog(matrix_sizes, results_ge, label="Gaussian Elimination")
    plt.legend()

```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->

## Exercise 2: LU factorisation with pivoting $\color{blue}{(\ast)}$

We can improve the stability of LU factorisation by additionally
including a pivoting step. In this way, we compute a factorisation:
$$
P A = L U.
$$

The new algorithm looks like:

1.  Initialise $P = I_n$ (the $n \times n$ identity), $L = O_n$ (the
    $n \times n$ zero matrix) and $U = O_n$.

2.  For $k = 1, \ldots, n$:

    1.  Find the pivot row $i$ with the largest
         $$\left| A_{ik} - \sum_{l=1}^{k-1} L_{il}U_{lk} \right|$$
        for $i \in {k,\ldots,n}$ — that is, compare column $k$'s entries after accounting for the eliminations from the previous $k-1$ columns, not $A$'s original entries. Swap rows $k$ and $i$ in $A$ and $L$ and store this swap in $P$.
    2.  Find the pivot row $i$ with the largest $|A_{ik}|$ for
        $i \in \{ k, \ldots, n \}$. Swap rows $k$ and $i$ in $A$ and $L$ and store this
        swap in $P$.
    3.  Set $L_{kk} = 1$.
    4.  Continue with LU factorisation in column $k$ as usual.
    5.  Repeat for next column $k+1$.

Implement this new method and test on the system of linear equations
given by:
$$
\begin{pmatrix}
10 & -7 & 0 \\ -3 & 2.1 - \varepsilon & 6 \\ 5 & -1 & 5
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\x_3
\end{pmatrix}
= \begin{pmatrix}
7 \\ 9.9 + \varepsilon \\ 11
\end{pmatrix}.
$$
Test with $\varepsilon = 10^{-15}$.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]

```
