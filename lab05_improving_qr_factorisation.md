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
# 
Theoretical Foundations of Computer Science II COMP2870

**School of Computer Science, University of Leeds**

## Lab 05: Improving QR factorisation
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
On-time submission date: **Friday 20 November 2026, 2:00pm**

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

These lab exercises cover the QR algorithm.

## Learning outcomes

On completion of this activity sheet you will have demonstrated that you can:

- Explain how the realisation of the Gram-Schmidt process in floating point numbers can lead to inaccurate results.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
## How to access the lab

You can access the lab worksheet directly through [minerva](https://minerva.leeds.ac.uk/), [github](https://github.com/COMP2870-2627/linear-algebra-student-labs) or using Noteable (accessible via Minerva - see `README.md` for detailed instructions).

These lab worksheets are written using ['Jupyter Notebooks'](https://jupyter.org/). Many, many tutorials and guides are [available online](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
import numpy as np
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
## Exercise 1: Problems with QR factorisation

<div class="alert alert-block alert-danger">
<b>Portfolio exercise</b>
You should submit two files:

1. A single Python (`.py`) file defining `gram_schmidt_qr(A)` and a
   `generate_table()` function. Calling `generate_table()` must build the
   table described below and save it to a file named `"table.csv"` in the
   working directory - the autograder looks for that exact filename, with
   columns `eps`, `error1`, `error2`, `error3` and one row per `eps` value.

   You might wish to use the template file `lab05_submission_template.py`.
   
2. A single Markdown (`.md`) or plain text (`.txt`) file containing your
   written explanation (Part 2 below).
</div>

The Gram-Schmidt process is known not to be numerically stable. In practice, this means that the method can have problems which lead to loss of orthogonality through the process. In this exercise, we will explore this problem on a simple $2 \times 2$ problem.

For $\varepsilon > 0$, let $A_\varepsilon$ be the matrix given by
$$
A_\varepsilon = \begin{pmatrix}
1 & 1 + \varepsilon \\
1 + \varepsilon & 1
\end{pmatrix}.
$$

There are three ways to judge the accuracy of a QR factorisation
$$
\begin{aligned}
\text{error}_1 &= \| A - QR \|_F \\
\text{error}_2 &= \| Q^T Q - I_{n} \|_F \\
\text{error}_3 &= \| R - \text{toupper}(R) \|_F,
\end{aligned}
$$
where $\| \cdot \|_F$ is a norm on matrices that can be computed using `np.linalg.norm(...)` and $\text{toupper}$ is a function that takes a matrix to only its upper triangular part which can be computed using `np.triu(...)`.

1. Create a table with the columns $\varepsilon$, $\text{error}_1$, $\text{error}_2$ and $\text{error}_3$ for $\varepsilon = 10^{-6}, 10^{-7}, \ldots, 10^{-16}$ using the classical Gram-Schmidt process from the lectures.
2. Explain how floating-point rounding errors affect the orthogonality of the computed basis vectors and identify which of the three error measures captures this effect most clearly.

<!-- #endregion -->

```python tags=["portfolio"]
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
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
## Exercise 2: Improving the QR algorithm

In this exercise, we will improve our implementation of
`gram_schmidt_eigen`.

Implement *one* of the following improvements and see how the change
affects the resulting performance of the algorithm in terms of robustness, accuracy
and/or efficiency.

1.  Following [Example
    7.3](https://comp2870-2627.github.io/linear-algebra-notes/src/lec07.html#exm-char),
    we have a good formula for how *shifting* a matrix changes the
    eigenvalues and eigenvectors of a matrix.

    For a shift value $\mu$, the key idea for the shifted algorithm is
    to shift the matrix before computing QR factorisation
    $$
    A - \mu I_n = QR,
    $$ and then undo the shift when updating
    $$
    A^{\text{new}} = RQ + \mu I_n.
    $$

    There are two suggestions from the literature to improve the speed
    of convergence.

    -   The first is to take the bottom right value of the matrix $A$ at
        each step $\mu = A_{nn}$. Note this value changes throughout the
        computation as we update $A$.
    -   The second is to use the *Wilkinson shift*. In this case, we
        compute the eigenvalues of the bottom-right $2 \times 2$
        submatrix of $A$ (using your code from Lab04) and then
        choose the eigenvalue closest to the bottom-right element of $A$
        as our value of $\mu$.

    Neither change affects how the matrix $V$ should be computed.

2.  We can also scale the matrix to be close to unit size. We again do
    this before the QR factorisation and then undo during reconstruction

    1.  Set $\alpha = \max_{ij} | A_{ij} |$ and
        $\tilde{A} = A / \alpha$.
    2.  Compute the QR factorisation of $\tilde{A} = QR$.
    3.  Update the $A$ as
        $$
        A^{\text{new}} = \alpha RQ
        $$

    This change does not affect how the matrix $V$ should be computed.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
Test your solution by finding the eigenvalues and eigenvectors of 10 randomly created symmetric matrices of sizes $n = 2, 4, 8, 16, 32$.
To get accurate results replace your own `gram_schmidt_qr` implementation with `numpy.linalg.qr`.
Comment on what you find.

For the method for the lectures and each approach you implement, make a table of problem size, average (mean) time taken, average QR iterations and maximum error as implemented by the `test_accuracy_of_eigensolve` function. Additionally, plot how the average time taken and average number of iterations scale with problem size for each method, using a log-log scale.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
# replicable random seed
np.random.seed(42)


def random_symmetric_matrix(n):
    S, _ = np.linalg.qr(np.random.standard_normal((n, n)))
    D = np.diag(np.random.choice(np.arange(1, 1000), n, replace=False))
    A = S.T @ D @ S
    return A


def test_accuracy_of_eigensolve(A, eigenvalues, eigenvectors):
    """
    test accuracy of solution of eigenvalue problem
    """
    residuals = []
    for i in range(len(eigenvalues)):
        residual = np.linalg.norm(
            A @ eigenvectors[:, i] - eigenvalues[i] * eigenvectors[:, i]
        )
        residuals.append(residual)
    return max(residuals)
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
If you have time, implement one or more additional updates, again
comparing against the test cases from the lecture notes.

What happens if you change the random matrices to use
```python
D = np.diag(np.random.choice(np.arange(1, 1000), n, replace=True))
```
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]

```
