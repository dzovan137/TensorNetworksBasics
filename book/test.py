import numpy as np


# define a vector of size 8 where the elements are integers between 1 and 8
A_vec = np.array([1,2,3,4,5,6,7,8])

# redefine the vector into a 3-rank tensors
A_ten = A_vec.reshape(2,2,2)

# reshape of a tensor from a 3 leg to 2 leg
A_ten_reshape = A_vec.reshape(d,d*d)
print("A tensor reshaped =")
print(A_ten_reshape)


# define the vector first 
A_vec = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

# redefine the vector into a 4-rank tensors
A_ten = A_vec.reshape(2,2,2,2)

# permutation of legs (transposition)
A_ten_trans = A_ten.transpose(3,0,1,2)

