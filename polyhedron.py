import numpy as np
import math

#Construct poyhedron via network constraints (need to be np.arrays for polyhedral_model)

# build it with residual arcs but make sure all residual arcs have capacity of 0 to begin with and update as take steps in algorithm
# start with nod arc incidence matrix A (this doesn't include slack arcs yet)
#node arc incidence matrix
A = np.array([[-1,1,0,0],[-1,0,1,0],[0,-1,1,0],[0,-1,0,1],[0,0,-1,1],[1,0,0,-1]]).transpose()
#flow balance and arc cap values (x arcs, s^+ arcs, s^- arcs)
b=[0,0,0,0]
d=[0,0,0,0,0,0,2,4,3,1,5, math.inf,0,0,0,0,0,0,0,0]


###might not need depending on how Chase's code runs
def build_res_net(A):
	for i in range(len(A[0,:])-1):
		new_col = -1*A[:,i]
		A = A.concate(new_col)
	return A

def add_slack_arcs(A):
	n = len(A)
	slack_mat = np.identity(n)
	A = np.concatenate((A,slack_mat), axis = 1)
	A = np.concatenate((A,-1*slack_mat), axis = 1)
	return A;

#build capacity constraints
def construct_B(columns, rows, x_arc_ub = 'False'):
	x_arcs = np.array(np.concatenate((np.identity(rows),np.zeros((rows,columns))), axis = 1))
	s_arcs = np.array(np.concatenate((np.zeros((columns,rows)),np.identity(columns)), axis = 1))


	#lower cap
	B = x_arcs
	#upper cap
	if x_arc_ub:
		B = np.concatenate((B,-1*x_arcs), axis = 0)
	
	#s^+ arcs
	B = np.concatenate((B, -1*s_arcs), axis = 0)
	#s^- arcs
	B = np.concatenate((B, -1*s_arcs), axis = 0)

	return B;


print('before slack vars: ',A)
A = add_slack_arcs(A)
print('after slack vars: ',A)

B = construct_B(6,4, 'True')
print('inequalities: ',B)
