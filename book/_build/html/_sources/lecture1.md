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

# Lecture 1 

In this lecture we define the concept of a 
- {ref}`def`

and introduce the two basic operations such as
- {ref}`reshape`
- {ref}`permutation`

(def)=
## Tensors and Tensor Networks 

**Tensors** are multi-dimensional arrays of numbers. Diagrammatically we denote a tensor as a filled in solid shape with legs. The legs of a tensor represent the order (rank) of the tensor. In particular, we denote

```{image} /images/def.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```

**Tensor networks** are comprised of multiple tensors, where the shared legs denote a *contraction* (or summation) over this index. Below we make the simplest possible example of a tensor network.  
 
```{image} /images/fig1.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```
More specifically, this tensor network implies a contraction and if we take the example of square matrices of size n by n we have
```{image} /images/fig2.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```
So we see that that tensor networks are nothing but a graphical language to tell us to do matrix-matrix multiplication. So each tensor network can be written down as a summation over selected indices. 

We can now provide further examples such as the one that involves more legs. In case of three leg tensor we can have.

```{image} /images/fig3.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```


### Python code
Lets get our feet wet by defining our first tensor in programming language Python! 

 
```{code-cell}
# import the library that allows us to deal with arrays efficiently
import numpy as np

# define a vector of size 8 where the elements are integers between 1 and 8
A_vec = np.array([1,2,3,4,5,6,7,8])

# redefine the vector into a 3-rank tensors
d = 2
A_ten = A_vec.reshape(d,d,d)

print("A vector = ", A_vec)
print("A tensor = ")
print(A_ten)

```


So what have we actually done? In particular

```{image} /images/fig4.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```

In this case one is able to visualize the values using 3 dimensions as there are only 3 legs (directions), but it is easy to see how this extends to multiple legs. One can think of each of the legs to represent the particular qubit! We shall illustrate that later.

```{note}
The given example of a vector is useful in the context of quantum information theory and quantum many-body physics. In particular, we have selected the approprite partition of the vector into a tensor with legs of dimension d = 2 (local Hilbert space dimension). 

**Exercise:** Define the correct reshape for
- any integer n qubits of local dimension d = 2 
- any arbitrary local Hilbert space dimension, e.g. qudits d = 3 

Provide graphical representation of the process. 

```
(reshape)=
## Reshape
The examples we provided above actually involve reshaping tensors. We can not only reshape vectors into tensor, but <u>we can reshape any tensor of any rank in any other ranked tensor</u> under the condition that the number of total entries (elements) does not change! Reshaping of a tensor is than just a different organization of smaller matrices, and does not lose us any initial information stored. 

Next, we provide the simplest example of a reshaped tensor with the accompaning code. 


```{image} /images/fig6.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```


### Python code

```{code-cell}

# reshape of a tensor from a 3 leg to 2 leg
A_ten_reshape = A_vec.reshape(d,d*d)
print("A tensor reshaped =")
print(A_ten_reshape)


```
```{note}
**Exercise:** Starting from a tensor with 7 legs and d = 2, reshape this tensor into one with 4 legs where

- second and third 
- fourth and fifth 
- sixth and seventh 

are reshaped together. Provide graphical representation of the process. 

What happens if we want to reshape not neighboring legs? (next chapter answers this question)

```

(permutation)=
## Permutation
It is useful to permute ("transpose") the legs of a tensor. In particular, we want to switch the positions of certain legs.  The permutation implies the following operation on tensors. 

```{image} /images/fig5.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```

### Python code
In python code this is

```{code-cell}

# permutation (transposition)
A_ten_trans = A_ten.transpose(0,2,1)

print("A tensor transposed = ")
print(A_ten_trans)

```
Notice that we have just shuffled some elements of the tensor around. All the values are still there, just in a different position as compared to our original tensor given above. Note that the transposition in Python start from 0 index, and the logic is obvious from the construction. In the transposition array we only have assign from where the old leg comes, and put into the order where we want it to be. Another example of the transposition is given below. 

```{image} /images/fig7.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```

```{note}
**Exercise1:** Provide the python code for example of 4 legs for the example above. 


**Exercise2:** Provide the python code for the transposing the following tensor A_{123456789} = A_{693751482}
```




