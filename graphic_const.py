import numpy as np
import math

###construct matrix for graphic matroid independent matroid polytope H-rep
def construct_B(columns, rows):
	x_arcs = np.array(np.concatenate(np.identity(columns), axis = 1))


	#lower cap
	B = -1*x_arcs
	#upper cap
	B = np.concatenate((B,x_arcs), axis = 0)


from itertools import product
for j in range(2,4)
	x = [i for i in product(range(2), repeat=j)]
	# for i in range(columns):
	# 	for j in range(columns):
	# 		x = np.zeros(columns,0)
	# 		x[i] = 1
	# 		B = np.concatenate((),axis=0)

	return B;