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
- {ref}`graphicalcontraction`
- {ref}`symboliccontraction`



(graphicalcontraction)=
## Binary Tensor Contraction - Graphical

Contraction algorithmically can be broken down to as series of steps. Lets look at the following example 

```{image} /images/lecture2fig1.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```


### Step 0
We first need to initialized the desired tensor. Using Python this is done as
#### Python code
```{code-cell}
# import the library that allows us to deal with arrays efficiently
import numpy as np

d = 2
# create two random tensors
A_vec = np.random.rand(d,d,d,d)
B_vec = np.random.rand(d,d,d,d)

```
where we (as an example) create two random rank-4 tensors. 


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
# transpose the generate vectors
A_vec1 = A_vec.transpose(0,2,1,3)
B_vec1 = B_vec.transpose(0,3,1,2)

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
# reshaping the tensors
A_vec2 = A_vec1.reshape(d**2,d**2)
B_vec2 = B_vec1.reshape(d**2,d**2)

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
# matrix-matrix multiplication
C_prim = A_vec2 @ B_vec2

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
# we need to keep wanted leg number of the tensor
C = C_prim.reshape(d,d,d,d)
print(C)
```

### Comparison with direct evaluation
We can perform the contraction in its full glory, i.e. over all the involved indices as

```{code-cell}
# define an empty 4-leg tensor
C_direct = np.zeros([d,d,d,d])

# loop over the indices
for i in range(0,d):
	for j in range(0,d):
		for k in range(0,d):
			for l in range(0,d):

				# perform the matrix-matrix multiplication explicitely
				for m in range(0,d):
					for n in range(0,d):

						C_direct[i,j,k,l] = C_direct[i,j,k,l] + A_vec[i,m,j,n]*B_vec[m,k,l,n]
				
				

print(C_direct)
```
As we can see the outputs are the same! This implies that binary contraction is well defined and proper algorithmic procedure to perform tensor contraction 

```{note}
**Exercise1:** Using python function *time* check how the binary tensor network contraction scales with increasing number of local dimension d as compared to the direct approach. Use *matplotlib* to present the scaling plots. 

```


(symboliccontraction)=
## Binary Tensor Contraction - Symbolic
Sometimes it is easier to take care of the indices symbolically rather graphical and the whole process can be represented as 


```{image} /images/lecture2fig6.png
:alt: def
:class: bg-primary mb-1
:width: 700px
:align: center
```
The final step is sometimes necessary depending on what kind of contraction and what kind of tensors are used. 

```{note}
**Exercise2:** Try to contract the following tensors A_{ijab} B_{kabl}. Verify that that in this case one has to perform an additional transposition (i.e. step 5) in order to obtain the correct result. 


```







