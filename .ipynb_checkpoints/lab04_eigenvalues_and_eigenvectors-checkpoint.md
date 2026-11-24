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

## Lab 04: Eigenvalues and eigenvectors
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
On-time submission date: *no submission*

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

This lab sheet covers materials on Complex Numbers and the definitions of eigenvalues and eigenvectors.

## Learning outcomes

On completion of this activity sheet you will have demonstrated that you can:

- Solve simple eigenvalue problems.
- Verify whether a given vector or value is an eigenvector or eigenvalue.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["header"] -->
## How to access the lab

You can access the lab worksheet directly through [minerva](https://minerva.leeds.ac.uk/), [github](https://github.com/COMP2870-2627/linear-algebra-student-labs) or using Noteable (accessible via Minerva - see `README.md` for detailed instructions).

These lab worksheets are written using ['Jupyter Notebooks'](https://jupyter.org/). Many, many tutorials and guides are [available online](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["portfolio"] -->
<div class="alert alert-block alert-danger">
<b>Portfolio exercise</b>

There are no portfolio exercises in this lab worksheet.
</div>
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
import numpy as np
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
## Exercise 1: Eigenvalues of $2 \times 2$ matrices

For $2 \times 2$ matrices, we can use the quadratic formula to directly
find eigenvalues of matrices. First, write down the quadratic equation
that the eigenvalues should solve and then implement this in Python
code. You should write a function which takes a $2 \times 2$ matrix
represented by a numpy array and return both eigenvalues.

Test your code with the matrices
$$
\begin{pmatrix}
9 & -2 \\ -2 & 6
\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}
0 & 1 \\ -1 & 0
\end{pmatrix}.
$$
Find the eigenvalues by hand first then check your code gives the same results.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
import numpy as np
import math

"""
    input: 2x2 matrix
    output: Eigenvalues of input
"""
def eigenValues(A):
    return (-(-A[0][0] - A[1][1]) + math.sqrt(((-A[0][0] - A[1][1])**2) - 4*((A[0][0]*A[1][1]) - (A[0][1]*A[1][0])))) / 2, (-(-A[0][0] - A[1][1]) - math.sqrt(((-A[0][0] - A[1][1])**2) - 4*((A[0][0]*A[1][1]) - (A[0][1]*A[1][0])))) / 2

A = np.array([[9,-2],[-2,6]])
print(eigenValues(A))
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
## Exercise 2: Verifying eigenvalues and eigenvectors

In the next lab session, we will be computing eigenvalues and eigenvectors of larger systems. In this exercise, you are tasked with writing two functions that verify either an eigenvalue or eigenvector of a matrix.

1. Complete these functions. Your functions should simply return `True` or `False` depending on the inputs. You may use other `numpy` functions such as `numpy.linalg.norm` or `numpy.linalg.det` which do not directly compute eigenvalues or eigenvectors.
<!-- #endregion -->

```python tags=["formative"]
def verify_eigenvalue(A, value): ...


def verify_eigenvector(A, vector): ...
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
2. Verify your eigenvalue code on the example from Exercise 1. Additionally, verify which of the following are eigenvectors of $A$:
    $\vec{x}^{(a, b)} = \begin{pmatrix} a \\ b \end{pmatrix}$ for $a, b = -3, -2, \ldots, 2, 3$
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]

```

<!-- #region tags=["formative"] -->
3. Verify that for the matrix generated by `generate_safe_system(100)`, the vector $\vec{x}$ with $x_k = \sin(k\pi/101)$ (for $k=1, \ldots, 100$) is an eigenvector.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
from scipy.sparse import diags


def generate_safe_system(n):
    """
    Generate a matrix A which is weakly diagonally dominant.

    Parameters:
        n (int): Size of the system (n x n)

    Returns:
        A (ndarray): n x n weakly diagonally dominant matrix
    """

    k = [np.ones(n - 1), -2 * np.ones(n), np.ones(n - 1)]
    offset = [-1, 0, 1]
    A = diags(k, offset).toarray()
    return A
```

```python tags=["formative"]

```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
## Exercise 3: Complex linear algebra $\color{blue}{(\ast)}$

Many of the methods we have developed so far can be applied to solve systems of linear equations with complex coefficients.

One thing to be aware of is that Python follows the engineering convention that the complex unit (that we called $i$) is denoted in code by `j`.

Write code that applies Gaussian elimination with pivoting to the system of linear equations given by
$$
\begin{pmatrix}
-4 + 5i & 9 + 4i & 4 + 4i & 8i & -3 + i \\
10 + 9i & -4 -8i & 8 - 6i & 8i & -4i \\
10 + 10i & -7 -2i & -3 -4i & -8 +7i & 10 - 7i \\
-9 + 3i & 1 + 7i & -5 -2i & -9 + 10i & 10 -9i \\
-10 + 9i & 1 + 4i & 1 -4i & 6 + i & -1 -3i
\end{pmatrix}
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix} =
\begin{pmatrix}
6 + 22i \\ 14 - i \\ 2 + 4i \\ -12 + 9i \\ -3 + 7i
\end{pmatrix}.
$$
Show that the solution is $\vec{x} = (1, 1, 1, 1, 1)^T$.
What condition should be used in place of the real absolute value when ranking complex pivot candidates?

*Hint*: Copy the code from the lecture notes ([4. Direct solvers for systems of linear equations](https://comp2870-2627.github.io/linear-algebra-notes/src/lec04.html)) and then update the code where necessary.
<!-- #endregion -->

```python tags=["formative"]
A = np.array(
    [
        [-4.0 + 5.0j, 9.0 + 4.0j, 4.0 + 4.0j, 0.0 + 8.0j, -3.0 + 1.0j],
        [10.0 + 9.0j, -4.0 - 8.0j, 8.0 - 6.0j, 0.0 + 8.0j, 0.0 - 4.0j],
        [10.0 + 10.0j, -7.0 - 2.0j, -3.0 - 4.0j, -8.0 + 7.0j, 10.0 - 7.0j],
        [-9.0 + 3.0j, 1.0 + 7.0j, -5.0 - 2.0j, -9.0 + 10.0j, 10.0 - 9.0j],
        [-10.0 + 9.0j, 1.0 + 4.0j, 1.0 - 4.0j, 6.0 + 1.0j, -1.0 - 3.0j],
    ]
)

b = np.array(
    [[6.0 + 22.0j], [14.0 - 1.0j], [2.0 + 4.0j], [-12.0 + 9.0j], [-3.0 + 7.0j]]
)
```

```python tags=["formative"]

```
