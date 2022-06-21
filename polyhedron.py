#Construct poyhedron via network constraints

# build it with residual arcs but make sure all residual arcs have capacity of 0 to begin with and update as take steps in algorithm
# start with nod arc incidence matrix (this doesn't include slack arcs yet)
def build_res_net(A):
	for i in range(len(A[0,:])):
		new_col = -1*A[:,i]
		A = A.concate(new_col)
return A

def add_slack_arcs(A):
	n = len(A[:,0])
	slack_mat = np.identity(n)
	A.concate(slack_mat)
	A.concate(-1*slack_mat)


#build capacity constraints
def construct_B(m,n):
	x_arcs=np.identity(n).concate(np.zeros((n,m)))
	s_arcs=np.zeros((m,n)).concate(np.identity(m))
	#lower cap
	B.concate(x_arcs)
	#upper cap
	B.concate(x_arcs)
	#s^+ arcs
	B.concate(s_arcs)
	#s^- arcs
	B.concate(s_arcs)


#flow balance and arc cap values
	b=[]
	d=[]

