# LECTURE 1

#import numpy as np


# define a vector of size 8 where the elements are integers between 1 and 8
#A_vec = np.array([1,2,3,4,5,6,7,8])

# redefine the vector into a 3-rank tensors
#A_ten = A_vec.reshape(2,2,2)

# reshape of a tensor from a 3 leg to 2 leg
#A_ten_reshape = A_vec.reshape(d,d*d)
#print("A tensor reshaped =")
#print(A_ten_reshape)


# define the vector first 
#A_vec = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

# redefine the vector into a 4-rank tensors
#A_ten = A_vec.reshape(2,2,2,2)

# permutation of legs (transposition)
#A_ten_trans = A_ten.transpose(3,0,1,2)


# LECTURE 2




import numpy as np
import time

d = 2
# create two random tensors
A_vec = np.random.rand(d,d,d,d)
B_vec = np.random.rand(d,d,d,d)

start_time = time.time()

A_vec1 = A_vec.transpose(0,2,1,3)
B_vec1 = B_vec.transpose(0,3,1,2)

A_vec2 = A_vec1.reshape(d**2,d**2)
B_vec2 = B_vec1.reshape(d**2,d**2)


C_prim = A_vec2 @ B_vec2

C = C_prim.reshape(d,d,d,d)

print("C =")
#print(C)
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()

C_direct = np.zeros([d,d,d,d])

for i in range(0,d):
	for j in range(0,d):
		for k in range(0,d):
			for l in range(0,d):

				for m in range(0,d):
					for n in range(0,d):

						C_direct[i,j,k,l] = C_direct[i,j,k,l] + A_vec[i,m,j,n]*B_vec[m,k,l,n]
				
				


print("C direct =")
#print(C_direct)
print("--- %s seconds ---" % (time.time() - start_time))
