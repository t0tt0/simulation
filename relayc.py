import numpy as np
# import scipy.optimize as op
import random
from inspect import getmembers
import pulp as pulp
import math
import time
from matplotlib import pyplot as plt

shardid = [] #for each v_t
initialindex = [] #for cross-
mycross = [] #for v_t
shardUp = [] #for regular shards
Uptrans = [] #for upshards
numUp = 2
workload = []
statusid = []
upcross = []


def lpprog1(numShard, numTrans, weights, res):
	# print(SSize)
	
	for i in range (len(weights)):
		weights[i] = weights[i]

	variables = [[pulp.LpVariable("x%d,%d"%(i, j) ,lowBound=0, cat='Continuous') for j in range(numTrans)] for i in range(numShard)]

	# print("variables done")

	
	

	prob = pulp.LpProblem('LP2', pulp.LpMinimize)

	
	c = sum(weights)/float(numShard)
	w = sum(weights)

	

	prob += pulp.lpSum( (variables[i/numTrans][i%numTrans])*(weights[i%numTrans]*(2**(weights[i%numTrans])))*(numTrans - i%numTrans - 1) for i in range(numShard*numTrans) )
	
	# print("objectives done")



	
	

	for t in range (numTrans):
		prob += pulp.lpSum(variables[s][t] for s in range(numShard)) == 1

	for s in range (numShard):
		# prob += pulp.lpSum(-variables[s][j]*weights[j] for j in range(numTrans)) <= SSize
		prob += pulp.lpSum(variables[s][j] for j in range(numTrans)) <= len(weights)/numShard
	


	# print("constraints done")

	ticksbefore = time.time()
	status = prob.solve()
	ticksafter = time.time()
	
	elap = ticksafter - ticksbefore

	total = 0


	# res = [[0 for i in range(numTrans)] for j in range(numShard)]

	
	sumtrans = 0
	ind = 0
	for var in prob.variables():
		res[ind/numTrans][ind%numTrans] = var.varValue
		ind = ind + 1

	

	# for i in range (numShard):
	# 	for j in range (numTrans):
	# 		# if status == 1:
	# 		# print pulp.value(variables[i][j]), 
	# 		sumtrans = sumtrans + res[i][j]
	# 	# if status == 1:
	# 	# print("\n")
	# print sumtrans


	loads = []
	pershard = 0
	nums =[]
	pers = 0
	for i in range (numShard):
		pershard = 0
		pers = 0
		for j in range (numTrans):
			total = total + res[i][j]*(weights[j])
			pershard = pershard + res[i][j]*(weights[j])
			pers = pers + res[i][j]
		loads.append(pershard)
		nums.append(pers)

	# print loads
	# print nums
	
	testva = 0
	for i in range (numTrans):
		testva = testva +  (weights[i])*(2*numTrans - 2*i - 1)

	# print "calculated objective is", pulp.value(prob.objective), "testva is = ", testva

	return total, max(loads), elap


def randomlyassignments(sumvt, numUp, numShard):
	# av = (numShard - numUp)/numUp
	av = 2
	numUp = int(numShard*0.25)
	base = numShard-numUp


	

	for i in range (numShard-numUp):
		if i/av >= numUp:
			shardUp.append(-1)
		else:
			shardUp.append(i/av)

	# print shardUp

	for i in range (numUp):
		Uptrans.append(0)

	# print numShard-numUp
	for i in range (sumvt):
		shardid.append(random.randint(0, (numShard-numUp-1))) #randomly assignments

	# print shardid, 


def cateassignment(sumvt, numShard):
	crosspiv = 0
	remax = (sumvt-2*numTrans)/(int(numShard-3))
	print(remax)
	# for i in range(sumvt):
	# 	if i == weights[crosspiv]: #registration trans
	# 		shardid.append(0)
	# 	elif i == weights[crosspiv - 1]:
	# 		shardid.append(numShard-1)
	# 		crosspiv = crosspiv + 1
	# 	else:
	# 		cusha = (i - crosspiv*2)/remax
	# 		shardid.append(cusha)

	# crosspiv = 0
	remaint = sumvt-2*numTrans
	print(remaint)



	workload11 = []

	for i in range (numShard):
		workload11.append(0)

	print workload11
	
	for i in range (numShard):
		if i ==0 :
			workload11[i] = numTrans
		elif i == numShard-1:
			workload11[i] = sumvt
		else:
			if remax <= remaint:
				workload11[i] = remax
				remaint = remaint - remax
			else:
				workload11[i] = remaint


	print (sumvt*20/float(max(workload11))) #resul



		




def inteassignments(sumvt, numTrans, numShard, weights):
#not randomly
	
	
	for i in range (sumvt):
		shardid.append(-1)

	res = [[0 for i in range(numTrans)] for j in range(numShard)]
	totallp, maxloadlp, elap = lpprog1(numShard, numTrans, weights, res)

	# print res

	for i in range (numShard):
		for j in range (numTrans):
			if res[i][j] == 0:
				continue
			for vt in range (weights[j]):
				vtid = initialindex[j] + vt
				shardid[vtid] = i
#not randomly


def initialize(numTrans, weights, numShard):


	sumvt = 0
	pivot = 0
	for i in range (numTrans):
		sumvt = sumvt + weights[i]
	
	

	for i in range (numTrans):
			initialindex.append(pivot)
			for j in range (weights[i]):
				mycross.append(i)
			pivot = pivot + weights[i]


	for i in range (numShard):
		workload.append(0)

	for i in range (sumvt):
		statusid.append(-2)


	
	randomlyassignments(sumvt, numUp, numShard)
	# cateassignment(sumvt, numShard)
	# inteassignments(sumvt, numTrans, numShard, weights)


	
	# for i in range (numShard):
	# 	for j in range (numTrans):
	# 		print res[i][j], 
	# 	print "\n"

	# print weights
	# print shardid 
	

def sameornot(vtid, weights, numShard, numUp):
	myid = shardid[vtid]
	neighid = -1
	mycrosst = mycross[vtid]
	starting = initialindex[mycrosst]
	if starting == vtid:
		return 1
	elif shardid[vtid] == shardid[starting]:
		return 0
	if shardid[vtid] != shardid[starting]:
		ressh = shardid[starting]
		currsh = shardid[vtid]

		resups = shardUp[ressh]
		currups = shardUp[currsh]
		# print resups, currups
		if resups == currups and resups != -1:
			Uptrans[resups] = Uptrans[resups] + 1
			shardid[vtid] = (numShard - numUp) + resups
			# print base 
			return 2
		return -1
	# for i in range(starting+1, starting+weights[mycrosst], 1):
	# 	neighid = shardid[i]
	# 	if neighid != myid:
	# 		return -1
	# return 1

def getTrans(weights, numTrans, AverageN, tms):
	sd = (tms - 1)*AverageN/3
	for i in range (numTrans):
		w = int(random.gauss(AverageN, sd))
		if w < 3:
			w = 3
		if w%2 == 0:
			w = w - 1
		# print w
		weights.append(w)


def getCross():


	numTrans = 100

	for avg in range (3, 10, 1):



		weights = []
		numShard = 2
		tms = 4
		getTrans(weights, numTrans, avg, tms)
		# print weights
		initialize(numTrans, weights, numShard)


		sumvt = 0
		for i in range (numTrans):
			sumvt = sumvt + weights[i]


		numcross = 0 
		# print shardid
		numIn = 0 #intra-shard

		# print statusid
		for i in range (sumvt):
			r = sameornot(i, weights, numShard, numUp)
			if r == -1: 
				numcross = numcross + 1
				statusid[i] = -1
			elif r == 0: #assigned non-res intra
				statusid[i] = 0	
				# numIn = numIn + 1
			elif r == 1: #regis
				statusid[i] = 1
			elif r == 2: #upshard intra
				statusid[i] = 2

		# print statusid

		for i in range (sumvt):
			myshard = shardid[i]
			if statusid[i] == 0: #intra- v_t
				workload[myshard] = workload[myshard] + 1
			if statusid[i] == 1: # i is reg
				workload[myshard] = workload[myshard] + 1
				crosst = mycross[i]
				ressha = shardid[i]
				if len(shardUp) == 0:
					continue
				resshup = shardUp[ressha]
				flag = 0
				for t in range (i+1, i + weights[crosst], 1):
					if resshup == -1:
						break
					vtsha = shardid[t]
					vtshaup = shardid[vtsha]
					if vtshaup == resshup and vtshaup != -1:
						flag = 1
				if flag == 1:
					workload[resshup] = workload[resshup] + 1
			if statusid[i] == 2:
				# print "xx"
				workload[myshard] = workload[myshard] + 1
			elif statusid[i] == -1:
				# print "xx"
				workload[myshard] = workload[myshard] + 2
				resid = mycross[i]
				ressh = shardid[resid]
				workload[ressh] = workload[ressh] + 1

		if len(initialindex) != 0:
			initialindex = []
			mycross = []
			workload = []
			statusid = []

		if len(shardid) != 0:
			shardid = []

		if len(shardUp) != 0:
			shardUp = []
			Uptrans = []
			upcross = []



		print (max(workload))
		print (numcross/float(sumvt))


if __name__ == "__main__":

	# getCross()


	weights = []
	numTrans = 1000
	AverageN = 3
	tms = 4
	numShard = 5

	getTrans(weights, numTrans, AverageN, tms)
	initialize(numTrans, weights, numShard)

	print (max(workload))
	# print res

	# print weights

	sumvt = 0
	for i in range (numTrans):
		sumvt = sumvt + weights[i]


	numcross = 0 
	numIn = 0 #intra-shard
	for i in range (sumvt):
		r = sameornot(i, weights, numShard, numUp)
		if r == -1: 
			numcross = numcross + 1
			statusid[i] = -1
		elif r == 0: #assigned non-res intra
			statusid[i] = 0	
			# numIn = numIn + 1
		elif r == 1: #regis
			statusid[i] = 1
		elif r == 2: #upshard intra
			statusid[i] = 2

	# print shardid

	for i in range (sumvt):
		myshard = shardid[i]
		if statusid[i] == 0: #intra- v_t
			workload[myshard] = workload[myshard] + 1
		if statusid[i] == 1: # i is reg
			workload[myshard] = workload[myshard] + 1
			crosst = mycross[i]
			ressha = shardid[i]
			if len(shardUp) == 0:
				continue
			resshup = shardUp[ressha]
			flag = 0
			for t in range (i+1, i + weights[crosst], 1):
				if resshup == -1:
					break
				vtsha = shardid[t]
				vtshaup = shardid[vtsha]
				if vtshaup == resshup and vtshaup != -1:
					flag = 1
			if flag == 1:
				workload[resshup] = workload[resshup] + 1
		if statusid[i] == 2:
			# print "xx"
			workload[myshard] = workload[myshard] + 1
		elif statusid[i] == -1:
			# print "xx"
			workload[myshard] = workload[myshard] + 2
			resid = mycross[i]
			ressh = shardid[resid]
			workload[ressh] = workload[ressh] + 1


	# # print Uptrans

	# print workload


	print (sumvt*20/float(max(workload))) #resul

	# print sumvt, numcross+ sum(Uptrans)+ numTrans+numIn

	print(numcross) #resul

