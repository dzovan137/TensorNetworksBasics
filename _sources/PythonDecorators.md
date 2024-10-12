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


## 2. Average Timer
```{code-cell}
import time
import numpy as np
from functools import wraps



def timer1(how_many_times):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            add = 0.0

            for i in range(0, how_many_times):

                before = time.time()
                f(*args, **kwargs)
                later = time.time() - before

                add = add + later

            add = add / how_many_times
            print("Averaged ", how_many_times, "time. Executed in:", add, "seconds")

            return f(*args, **kwargs)

        return decorated_function

    return decorator



@timer1(10)
def diag1(size: int):

    # Generate a random symmetric matrix
    A = np.random.rand(size, size)
    A = (A + A.T) / 2  # Make the matrix symmetric

    # Diagonalize using eigh (for Hermitian matrices)
    eigenvalues, eigenvectors = np.linalg.eigh(A)



diag1(500)


```






## 3. Logger
```{code-cell}
import datetime


def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write(
                "Called function with "
                + " ".join([str(arg) for arg in args])
                + " at "
                + str(datetime.datetime.now())
                + "\n"
            )
            val = func(*args, **kwargs)
            return val

    return wrapper


@log
def run(a, b, c):
    print(a + b + c)


run(1, 2, 3)


```




