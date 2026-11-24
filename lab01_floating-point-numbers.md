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

## Lab 01: Floating-point numbers
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

<!-- #region editable=true jp-MarkdownHeadingCollapsed=true slideshow={"slide_type": ""} tags=["header"] -->
## Coursework summary

These lab exercises cover material not covered in the lectures. Supporting written material is available at [2  Floating point number systems](https://comp2870-2627.github.io/linear-algebra-notes/src/lec02.html).

## Learning outcomes

On completion of this activity sheet you will have demonstrated that you can:

- explain practical challenges working with floating-point numbers
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

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
## Exercise 1:

Write a for loop to add
`0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1` (i.e. `0.1`
10 times). What value do you get and why?
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
total = 0

for i in range(10):
    total += 0.1
    total
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
## Exercise 2:

Given an algorithm which gives *computed answer* as an approximation to
an *exact answer*, we define two errors:
$$
\begin{aligned}
\text{Absolute error} & = |\text{computed answer} - \text{exact answer}| \\
\text{Relative error} & = \frac{|\text{computed answer} - \text{exact answer}|}{| \text{exact answer}|}.
\end{aligned}
$$

Recall derivatives of a smooth function
$f \colon \mathbb{R} \to \mathbb{R}$ can be computed by finding the
limit
$$
f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}.
$$
We can use the *finite difference method* which computes an
approximation to derivatives through replacing the limiting process by
taking a small value for $\Delta x$:
$$
\text{approx} = \frac{f(x + \Delta x) - f(x)}{\Delta x}.
$$

Write code to approximate the derivative using finite differences of
$f(x)$ at a point $x$.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
def df(f, x, delta_x): ...
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
First use $x = 1$ and $f(x) = x^4$. Produce a table of values of $\Delta x$, the finite difference approximation the derivative at each
point, as well as the absolute and relative errors. Use
$\Delta x = 10^{-j}$ for $j = 3, 4, 5, 6, \ldots, 19$.

Which value of $\Delta x$ gives the best value of the derivative at each
point? Investigate what goes wrong for values of $\Delta x$ smaller than
the best value.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]

```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
Repeat the analysis at $x = 100$. What differences do you observe?
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]

```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
## Exercise 3:

The [Basel problem](https://en.wikipedia.org/wiki/Basel_problem) is the
problem of finding the sum:
$$
\sum_{n=1}^\infty \frac{1}{n^2} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \cdots = \frac{\pi^2}{6} \approx 1.644934
$$

Write Python code to find the sum above replaced by the partial sum:
$$
S_N = \sum_{n=1}^N \frac{1}{n^2} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \cdots + \frac{1}{N^2}.
$$
Compute the values of $S_{10^7}$, $S_{10^8}$ and $S_{10^9}$ and
compute absolute errors to $\pi^2/6$.

How do the errors change if you reverse and instead start from the
largest values of $n$ in the sum? Why?
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]

```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
## Exercise 4: $\color{blue}{(\ast)}$

Archimedes approximated $\pi$ by determining lengths of the perimeters
of polygons inscribing and circumscribing a circle of diameter 1.
Starting with the hexagon and successively doubling the number of sides,
we have the recurrence formula for the side length in the circumscribed
polygon, at step $n+1$,
$$
\begin{aligned}
p_{n+1} & = \frac{ \sqrt{p_n^2+1} - 1 }{ p_n } && \text{ for } n=0,1,2,\ldots \\
p_0 & = \frac{1}{\sqrt{3}}.
\end{aligned}
$$
Thus $\pi$ can be found as a limit, noticing that the number of sides
is $6 \cdot 2^n$,
$$
\pi = \lim_{n \to \infty} 6 \cdot 2^n \cdot p_n = 3.141592653589793\ldots 
$$

We can use this iteration to write code to compute $\pi$ using:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]
import numpy as np


def side_length(n):
    """
    Compute the length of one side of a polygon with 6*2**n sides.

    ARGUMENTS:  n  nonnegative integer to calculate number of sides.

    RETURNS:    float
    """
    assert n >= 0

    if n == 0:
        return 1.0 / np.sqrt(3.0)

    p = side_length(n - 1)
    return (np.sqrt(p * p + 1.0) - 1.0) / p


def pi_approx(n):
    """
    Compute an approximation to pi using polygonal approximations of
    a circle.

    ARGUMENTS:  n nonnegative integer

    RETURNS:    float approximation of pi
    """
    return 6.0 * 2**n * side_length(n)
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["formative"] -->
1.  Produce a table of values of `n`, `pi_approx(n)` and the error
    between $\pi$ and its approximation for `n` between 0 and 50
    inclusive. How many correct digits can you achieve?

2.  Iterating further after the best approximation, what would you see?
    Why?

3.  Consider an alternative way of writing the update formula for $p_n$:
    $$
    p_{n+1} = \frac{p_n}{ \sqrt{p_n^2 + 1} + 1 } \quad \text{ for } n=0,1,2,\ldots
    $$
    The reformulation is achieved by rationalising the numerator.
    Implement this new formula. Produce a table of values of `n`,
    `pi_approx(n)` and the error between $\pi$ and its approximation for
    `n` between 0 and 50 inclusive.

4.  How many correct digits can you achieve now? If you make more and
    more iterations after the best approximation, comment on what you
    observe by considering each term in your iteration formula.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["formative"]

```
