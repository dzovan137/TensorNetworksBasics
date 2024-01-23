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

# Lecture 2

In this lecture we perform  tensor network contraction explicity
- {ref}`manualcontraction`
- {ref}`automaticcontraction`



(manualcontraction)=
## Binary Tensor Contraction

Contraction algorithmically can be broken down to as series of steps. Lets look at the following example 

```{image} /images/lecture2fig1.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```

Before proceeding we create the tensors displayed above using python as
```{code-cell}
# import the library that allows us to deal with arrays efficiently
import numpy as np

# create two random tensors
A_vec = np.random.rand(2,2,2,2)
B_vec = np.random.rand(2,2,2,2)

```
where we create two random rank-4 tensors. 
### Step 0
We first need to initialized the desired tensor. Using Python this is done as
#### Python code
```{code-cell}
# import the library that allows us to deal with arrays efficiently
import numpy as np

# create two random tensors
A_vec = np.random.rand(2,2,2,2)
B_vec = np.random.rand(2,2,2,2)

```
where we create two random rank-4 tensors. 


### Step 1
We first perform a transposition of the the two tensors A and B in the following way

```{image} /images/lecture2fig2.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```
where we obtained new A and B that have elements shuffled. The main idea is that need to shuttle (transpose or permute) the target contraction indices for the matrix A to right, while for the B matrix we have to shuttle (transpose or permute) the contraction indices to left.  

#### Python code
Lets get our feet wet by defining our first tensor in programming language Python! 

 
```{code-cell}
# import the library that allows us to deal with arrays efficiently
import numpy as np

```


### Step 2
Afterwards we reshape the new A and B tensors in such a way 

```{image} /images/lecture2fig3.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```
Here the idea is that we 

#### Python code
Lets get our feet wet by defining our first tensor in programming language Python! 

 
```{code-cell}
# import the library that allows us to deal with arrays efficiently
import numpy as np

# define a vector of size 8 where the elements are integers between 1 and 8
A_vec = np.array([1,2,3,4,5,6,7,8])



```

### Step 3
After reshape we indices J have the same dimension and we can perform matrix-matrix multiplication over that index

```{image} /images/lecture2fig4.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```


#### Python code
Lets get our feet wet by defining our first tensor in programming language Python! 

 
```{code-cell}
# import the library that allows us to deal with arrays efficiently
import numpy as np

# define a vector of size 8 where the elements are integers between 1 and 8
A_vec = np.array([1,2,3,4,5,6,7,8])


```



### Step 4
We do a final reshape of the tensor to the desired number of legs as

```{image} /images/lecture2fig5.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```


#### Python code
Lets get our feet wet by defining our first tensor in programming language Python! 

 
```{code-cell}
# import the library that allows us to deal with arrays efficiently
import numpy as np

# define a vector of size 8 where the elements are integers between 1 and 8
A_vec = np.array([1,2,3,4,5,6,7,8])


```

### Symbolic representation of the algorithm
Sometimes it is easier to take care of the indices symbolically rather graphical and the whole process can be represented as 


```{image} /images/lecture2fig6.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```
The final step is sometimes necessary depending on what kind of contraction and what kind of tensors are used. 

```{note}
**Exercise1:** Contract one example where there is a violation of order of indices. 



```


(automaticcontraction)=
## Automatic Contraction Tool (Gven Evenbly)





