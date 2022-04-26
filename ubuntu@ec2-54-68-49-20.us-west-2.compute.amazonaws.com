import numpy as np
# import scipy.optimize as op
import random
from inspect import getmembers
import pulp as pulp

def greedy(weights, numShard):


	load = []
	numin = []
	averagein = []

	numTrans = len(weights)

	for i in range (numShard):
		load.append(0)
		numin.append(0)
		averagein.append(0)

	
	for i in range (numTrans):
		least = min(load)
		indexle = load.index(least)

		load[indexle] = load[indexle] + weights[i]
		numin[indexle] = numin[indexle] + 1


	# print load

	# for i in range (len(load)):
	# 	averagein[i] = load[i]/float(numin[i])

	# print numin

	# print averagein

	# print max(load), min(load)

	return max(load)


def getTrans(weights, numTrans, AverageN):
	for i in range (numTrans):
		w = int(random.gauss(AverageN, AverageN))
		if w < 4:
			w = 4
		# print w
		weights.append(w)

def solve_ilp(objective , constraints):
    
    # print constraints
    prob = pulp.LpProblem('LP1' , pulp.LpMaximize)
    prob += objective
    for cons in constraints :
        prob += cons
    # print prob
    status = prob.solve()
    if status != 1:
        #print 'status'
        #print status
        return None
    else :
        #return [v.varValue.real for v in prob.variables()]
        return [v.varValue.real for v in prob.variables()]


def lpprog(numShard, numTrans, weights, SSize):

	print ("ss")
	print SSize
	variables = [pulp.LpVariable('a%d'%i , lowBound = 0 , cat = pulp.LpBinary) for i in range(0 , numShard*numTrans)]
	print("variables done")
	# print variables
	# c = [3 , 4 , 5]
	objective = sum([variables[i] for i in range(0 , numShard*numTrans)])

	print("objective done")
	# print objective

	constraints = []

	# a1 = [1 , 2 , 0]
	for s in range (numShard):
		# pulp.lpSum(var[i]) <= x_max[i]
		print SSize
		constraints.append(sum([weights[t]*variables[s*numTrans + t] for t in range(0 , numTrans)]) <= SSize)
	
	print constraints

	for t in range (numTrans):
		constraints.append(sum([variables[s*numTrans + t] for s in range(0 , numShard)]) <= 1)
	# a2 = [0 , 1 , 3]
	# constraints.append(sum([a2[i]*variables[i] for i in range(0 , V_NUM)]) <= 40)
	
	


	res = solve_ilp(objective, constraints)
	# print res


if __name__ == "__main__":

	

	weights = []

	numTrans = 20
	numShard = 10
	AverageN = 10 #trans weight

	getTrans(weights, numTrans, AverageN)

	grload = greedy(weights, numShard)

	opb = grload/2

	# print opb


	total = sum(weights)

	mid = (opb+grload)/2
	lower = opb
	upper = grload

	# print mid

	pulp.pulpTestAll()
	# for m in getmembers(pulp.solvers):
	# 	if isinstance(m[1], type):
	# 		print('--', m[1]().available(), m)
	# 	continue

	# solver_list = pulp.listSolvers(onlyAvailable=True)

	# print solver_list
	# lpprog(numShard, numTrans, weights, grload)

	# while 1:
	# 	lpre = lpprog(numShard, numTrans, weights, mid)
	# 	if lpre = total:
	# 		upper = mid
	# 		lower = lower
	# 		mid = (upper + lower)/2
	# 	else if lpre < total:
	# 		lower = mid
	# 		upper = upper
	# 		mid = (lower + upper)/2
	# 	if (mid - opb)/opb < 0.01 && lpre == total:
	# 		break 




	# print(" greedy done!")

