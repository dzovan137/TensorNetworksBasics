---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Python Decorators

Here we introduce the concept of decorators, and provide two simple examples of usage. 

## 1. Timer
```{code-cell}
import time
import numpy as np


def timer(func):
    def wrapper(*args, **kwargs):

        before = time.time()
        func(*args, **kwargs)
        print("Executed in:", time.time() - before, "seconds")

    return wrapper


@timer
def diag(size: int):

    # Generate a random symmetric matrix
    A = np.random.rand(size, size)
    A = (A + A.T) / 2  # Make the matrix symmetric

    # Diagonalize using eigh (for Hermitian matrices)
    eigenvalues, eigenvectors = np.linalg.eigh(A)


diag(500)

```


## 2. Logger



```{note}
**Exercise1:** Verify that that the code outputs values consistent with the Wigner semi-circle law.

**Exercise2:** Verify that the values have zero mean value and standard deviation (sqruare root of variance) equal to 1.

**Exercise3:** Implement the same code for the real symmetric (GOE) ensemble.

**Exercise4:** Check if the spacings follow the Wigner surmise.

**Exercise5:** In what situations we get the Poisson distribution? Make a code for that.






```



