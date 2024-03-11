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


# GUE (GAUSSIAN UNITARY ENSAMBLE)
def GUE_ensamble_generate(N: int,T: int):
    """
    Generates a list of eigenvalues that are generated by diagonalization of an
    ensemble of random matrices from the Gaussian Unitary Ensemble (GUE). 
    
    In the limit of large matrices and large ensembles this function follows the Wigner Dyson statistics.
    
    See Chapter 1 of  Livan, G., Novaes, M. & Vivo, P. Introduction to Random Matrices: Theory and Practice. (Springer International Publishing, 2018). doi:					10.1007/978-3-319-70885-0.


    Args:
        N (integer): Size of the square random matrices
        T (integer): Number of random matrices in the ensemble.

    Returns:
        values (list of floats): 1D array containing the sorted eigenvalues of the ensemble.


    Example:
	aa = GUE_ensamble_generate(100,10)
	print(aa)
    """



    values = np.zeros(N*T)
    counter = 0
    for i in range(0,T):
        # generate random matrix
        s = np.random.normal(0,1,(N,N)) + np.random.normal(0,1,(N,N))*1j

        # after we generate the matrix we symmetrize it so we dont have complex eigenvalues
        s_symmetric = (s + np.conjugate(np.transpose(s)) )/(2.0)

        # diagonalize to obtain the real eigenvalues
        w = np.linalg.eigvals(s_symmetric)

        ww = np.sort(w)

        # write down the values in an array
        for j in range(0,N):

            values[counter] = ww[j]
            counter = counter + 1

    return np.array(values)/np.sqrt(N)


aa = GUE_ensamble_generate(100,10)
print(aa)
print(np.std(aa))

