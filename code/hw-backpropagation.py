# Datamining Assignment
# Eungchan Kim
# 2013.03.03
 
# initial variable
O = [1,2,0.7311,0.0179,0.9933,0.8387] # output value
W = [[0,0,-3,2,4,0],[0,0,2,-3,0.5,0],[0,0,0,0,0,0.2],[0,0,0,0,0,0.7],[0,0,0,0,0,1.5]] #weight value
N = [[2,3,4],[2,3,4,],[5],[5],[5]] #uni directed network
E = [0,0,0,0,0,0] # Err value init

# fucntions
# calculate Err of last node
def last_err(i, true):
	return O[i]*(1-O[i])*(true-O[i])
# calculate Err
def curr_err(i):
	sum_weighted_err =0
	for node_num in N[i]:
		sum_weighted_err += E[node_num]*W[i][node_num]
	return O[i]*(1-O[i])*sum_weighted_err
# calculate new weight
def new_weight(i,j):
	W[i][j] += 10*E[j]*O[i]


if __name__ == "__main__":
	f = open('nn-train.txt','w')
	# output: node 6
	E[5] = last_err(5,0)
	# hidden layer: node 5,4,3
	for i in range(0,3):
		E[4-i] = curr_err(4-i)

	# print Err
	for i in range(6):
		print >> f, 'err_%(index)d: %(err)f' % {'index':6-i, 'err':E[5-i]}
	
	# new weight
	for i in range(5):
		for j in range(6):
			if W[i][j] != 0:
	 			new_weight(i,j)
 
	# print Weight
	for i in range(5):
		for j in range(6):
			if W[4-i][5-j] != 0:
				print >> f, 'w_%(i)d%(j)d = %(w)f' % {'i':5-i,'j':6-j,'w':W[4-i][5-j]}
