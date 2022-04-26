import numpy as np
# import scipy.optimize as op
import random
from inspect import getmembers
import pulp as pulp
import math
import time
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter



def greedy(weights, numShard, array):


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
		array[indexle][i] = 1


	return max(load)

def greedywithcons(weights, numShard, array):


	load = []
	numin = []
	averagein = []
	avaliable = []
	cu = []

	# weights.sort(reverse = True)

	random.shuffle(weights)

	numTrans = len(weights)

	for i in range (numShard):
		load.append(0)
		numin.append(0)
		averagein.append(0)
		avaliable.append(1)
		cu.append(0)
		

	
	for i in range (numTrans):
		least = min(cu)
		indexle = load.index(least)



		load[indexle] = load[indexle] + weights[i]
		numin[indexle] = numin[indexle] + 1

		if numin[indexle] == len(weights)/numShard:
			avaliable[indexle] = 0
			indexincu = cu.index(least)
			cu.pop(indexincu)
		else:
			indexincu = cu.index(least)
			cu[indexincu] = cu[indexincu] + weights[i]
		array[indexle][i] = 1


	return max(load)


def randomwithconstraints(weights, numShard, array):
	load = []
	numin = []
	averagein = []
	avaliable = []
	cu = []

	# weights.sort(reverse = True)
	random.shuffle(weights)

	numTrans = len(weights)

	piv = 0

	for i in range (numShard):
		load.append(0)
		numin.append(0)
		averagein.append(0)
		avaliable.append(1)
		cu.append(0)
		
	# print len(weights)/numShard
	
	for i in range (numTrans):

		if numin[piv] == (len(weights)/numShard):
			piv = piv + 1
			load[piv] = load[piv] + weights[i]
			numin[piv] += 1
		else:
			load[piv] = load[piv] + weights[i]
			numin[piv] += 1
		# else:
		array[piv][i] = 1


	return max(load)


def greedyonlyconstraints(weights, numShard, array):
	load = []
	numin = []
	averagein = []
	avaliable = []
	cu = []

	weights.sort(reverse = True)

	numTrans = len(weights)

	piv = 0

	for i in range (numShard):
		load.append(0)
		numin.append(0)
		averagein.append(0)
		avaliable.append(1)
		cu.append(0)
		
	# print len(weights)/numShard
	
	for i in range (numTrans):

		if numin[piv] == (len(weights)/numShard):
			piv = piv + 1
			load[piv] = load[piv] + weights[i]
			numin[piv] += 1
		else:
			load[piv] = load[piv] + weights[i]
			numin[piv] += 1
		# else:
		array[piv][i] = 1


	return max(load)


def getTrans(weights, numTrans, AverageN, tms):
	sd = (tms - 1)*AverageN/3
	for i in range (numTrans):
		w = int(random.gauss(AverageN, sd))
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
        # print(".......")
        return None
    else :
        #return [v.varValue.real for v in prob.variables()]
        return [v.varValue.real for v in prob.variables()]

def solve_lp(objective , constraints):
    
    # print constraints
    # print "hh"
    prob = pulp.LpProblem('LP2' , pulp.LpMinimize)
    prob += objective
    for cons in constraints :
        prob += cons
    # print prob
    # print "hhh"
    status = prob.solve()
    
    return status
   #  if status != 1:
   #      #print 'status'
   #      print status
   #      # print(".......")
   #      return None
   #  else :
   #      #return [v.varValue.real for v in prob.variables()]
   #      variables = prob.variables()
   #      print "optimal solution..."
   #      for i in range (numShard):
			# for j in range (numTrans):
			# 	print pulp.value(variables[i][j])
			# 	# sumtrans = sumtrans + pulp.value(variables[i][j])
			# # print("\n")
   #      return [v.varValue.real for v in prob.variables()]


def lpprog1(numShard, numTrans, weights, SSize):
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
		prob += pulp.lpSum(variables[s][j] for j in range(numTrans)) >= 0
	


	# print("constraints done")

	
	    

	ticksbefore = time.time()
	status = prob.solve()
	ticksafter = time.time()
	
	elap = ticksafter - ticksbefore

	total = 0


	res = [[0 for i in range(numTrans)] for j in range(numShard)]

	
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

	# print res
	
	testva = 0
	for i in range (numTrans):
		testva = testva +  (weights[i])*(2*numTrans - 2*i - 1)

	print "calculated objective is", pulp.value(prob.objective), "testva is = ", testva

	return total, max(loads), elap




def ilpprog(numShard, numTrans, weights, SSize):

	starttime = time.time()
	print ("ss")
	# print(SSize)
	# variables = [pulp.LpVariable('a%d'%i , lowBound = 0 , cat = pulp.LpBinary) for i in range(0 , numShard*numTrans)]
	variables = [[pulp.LpVariable("x%d,%d"%(i, j) , cat=pulp.LpBinary) for j in range(numTrans)] for i in range(numShard)]


	print("variables done")
	# print variables
	# c = [3 , 4 , 5]

	he = [[0 for i in range(numTrans)] for j in range(numShard)]

	for i in range (numShard):
		for j in range (numTrans):
			he[i][j] = 1

	objective = pulp.lpDot(variables, he)
	# objective = sum([variables[i] for i in range(0 , numShard*numTrans)])

	print("objective done")
	# print objective

	constraints = []

	
	hel = []
	for i in range (numTrans):
		hel.append(1)

	for t in range (numTrans):
		constraints.append(pulp.lpDot(hel, [row[t] for row in variables]) <= 1)
		# constraints.append(sum([variables[s*numTrans + t] for s in range(0 , numShard)]) <= 1)

	# print
	h = []
	for i in range (numTrans):
		h.append(1)

	for s in range (numShard):
		constraints.append(pulp.lpDot(variables[s], h) <= (len(weights)/numShard) )


	# for s in range (numShard):
	# 	# prob += pulp.lpSum(-variables[s][j]*weights[j] for j in range(numTrans)) <= SSize
	# 	prob += pulp.lpSum(variables[s][j] for j in range(numTrans)) <= len(weights)/numShard


	# 	# pulp.lpSum(var[i]) <= x_max[i]
	# 	# print(SSize)
	# 	constraints.append(sum([weights[t]*variables[s*numTrans + t] for t in range(0 , numTrans)]) <= SSize)

	# print constraints



	print("constraints done ")
	print(len(constraints))
	# for s in range (numShard):
	# 	# pulp.lpSum(var[i]) <= x_max[i]
	# 	# print(SSize)
	# 	constraints.append(sum([weights[t]*variables[s*numTrans + t] for t in range(0 , numTrans)]) <= SSize)
	
	# print constraints

	res = solve_ilp(objective, constraints)

	total = 0

	# ts = []
	# for v in variables:
	# 	ts.append(v.varValue.real)

	loads = []
	pershard = 0
	for i in range (numShard):
		pershard = 0
		for j in range (numTrans):
			total = total + pulp.value(variables[i][j]*weights[j])
			pershard = pershard + pulp.value(variables[i][j]*weights[j])
		loads.append(pershard)

	stoptime = time.time()
	elaps = stoptime - starttime
	# print total


	return total, max(loads), elaps




def allinone( numShard, numTrans, AverageN, tms):

	weights = []


	getTrans(weights, numTrans, AverageN, tms)

	

	arraynono = [[0 for i in range(numTrans)] for j in range(numShard)]

	timeb = time.time()
	grload = greedy(weights, numShard, arraynono)
	timea = time.time()

	grload2 = greedywithcons(weights, numShard, arraynono) + max(weights)*5

	arraynonono = [[0 for i in range(numTrans)] for j in range(numShard)]
	ws = greedyonlyconstraints(weights, numShard, arraynonono)
	

	# print 'mmm', timea-timeb
	# weights.sort(reverse = True)
	arrayo = [[0 for i in range(numTrans)] for j in range(numShard)]
	rando =randomwithconstraints(weights, numShard, arrayo) + max(weights)*10

	

	

	opb = grload/2

	


	total = sum(weights)

	mid = (opb+grload)/2
	lower = opb
	upper = grload

	

	
	maxcount = 49
	count = 0
	telap = 0
	

	
	totallp, maxloadlp, elap = lpprog1(numShard, numTrans, weights, grload)
	# totallp, maxloadlp, elap =  ilpprog(numShard, numTrans, weights, grload)
	# telap = elap

	
	print("count "), count, "time needed", elap, "avera = ", (total)/float(numShard)
	print("greedy result = "), (grload2), "greedy total = ", total
	print("random result = "), (rando), "greedy total = ", total
	print("lp result = "), (maxloadlp), "lp total =", totallp, ", ", mid
	print "done..."


	if grload2 <= maxloadlp:
		return -1, grload2, maxloadlp, rando, ws, (total)/float(numShard), elap

	return 1, grload2, maxloadlp, rando, ws, (total)/float(numShard), elap
	# print("greedy result = "), (grload), "greedy total = ", total
	# print("lp result = "), (maxloadlp), "lp total =", totallp
	
	
	# while 1:
	# 	# print mid
	# 	totallp, maxloadlp, elap = lpprog1(numShard, numTrans, weights, mid)
	# 	totallp = -totallp
	# 	maxloadlp = -maxloadlp
	# 	telap = telap + elap
		
	# 	if totallp == total:
			
	# 		upper = mid
	# 		lower = lower
	# 		mid = (upper + lower)/2
	# 	elif totallp < total:
	# 		lower = mid
	# 		upper = upper
	# 		mid = (lower + upper)/2
	# 	if(totallp < total):
	# 		print mid, grload, opb, totallp, total
	# 		count = count + 1
	# 	if(abs(totallp) - total > -0.1):
	# 		break
	# 	elif(count == maxcount):
	# 		break
		

	print("count "), count, "time needed", telap
	print("greedy result = "), (grload), "greedy total = ", total
	print("lp result = "), (maxloadlp), "lp total =", totallp, ", ", mid
	print "done..."


def changex(xti, position):
	return xti/int(10)

if __name__ == "__main__":


	Maxcount = 5
	c = 0
	acc = 0
	uopt = []
	gr = []
	lp = []
	ran = []
	wss = []
	uoo = []

	tc = []
	weixx = []
	tmsxx = []
	avvg = 0
	avvl = 0
	avvt = 0


	
	numTrans = 3000
	numShard = 10
	AverageN = 50 #trans weight
	
	print "tt"
	# allinone(numShard, numTrans, 10, 4)




	# grd = [8075, 12285, 16356, 20566, 24642, 28636, 32832, 37099, 41413, 45293, 49666, 53711, 57520, 61234, 65676, 70174, 74359, 78407]
	# lpm = [3477.8, 5178.9, 7008.8, 8994.8, 10590.9, 12301.0, 14059.0, 15697.1, 17598.3, 19200.5, 21219.5, 22838.1, 24567.0, 26166.2, 28062.6, 29982.3, 31666.0, 33540.5]

	# cvt = [1.3553111553192139, 1.3703834533691406, 1.3579181671142577, 1.3612987041473388, 1.3743816137313842, 1.373611330986023, 1.3708587646484376, 1.3646210432052612, 1.3692148208618165, 1.363743782043457, 1.3673300981521606, 1.3650275945663453, 1.4336584091186524, 1.4149624824523925, 1.4231336116790771, 1.357112956047058, 1.372006893157959, 1.3532567024230957]

	# # weixxx = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
	# # for wei in range (10, AverageN, 5):
	# # 	weixxx.append(wei)

	# # print weixxx
	# weixxx = np.arange(10,60, 5)
	# fig,ax = plt.subplots(1, 1, figsize = (10,5))

	# line1 = ax.bar(weixxx, grd[0:10], label='Greedy Algorithm', linestyle='--', color='red', linewidth = 5)
	# line2 = ax.bar(weixxx + 0.5, lpm[0:10], label = 'Linear Programming', linestyle='-.', color = 'blue', linewidth = 5)

	# # ax.set_xticks(np.arange(10, AverageN, 5))
	# # ax.set_yticks(np.arange(3000, 80000, 	))

	# ax.xaxis.set_tick_params( labelsize=20)
	# ax.yaxis.set_tick_params( labelsize=20)

	# ax.set_xlabel('average confirmations per $T$', fontsize = 30, labelpad = 20)
	# ax.set_ylabel('maximum load', fontsize = 30, rotation = 90, labelpad = 20)

	# ax.legend(loc="lower right")

	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	# plt.savefig('simulp.pdf', bbox_inches = 'tight')




	for wei in range (AverageN, AverageN, 5):
		print"current weights", wei
		c = 0
		avvg = 0
		avvl = 0
		avvr = 0
		avvw = 0
		avvo = 0

		avvt = 0
		acc = 0
		while 1:
			status, grload, maxloadlp, rando, ws, uo, elap = allinone(numShard, numTrans, wei)
			if status == 1:
				avvg = avvg + grload
				avvl = avvl + maxloadlp
				avvt = avvt + elap
				avvr = avvr + rando
				avvw = avvw + ws
				avvo = avvo + uo
				acc = acc + 1
			c = c + 1
			if c == Maxcount:
				avvg = avvg/acc
				avvl = avvl/acc
				avvt = avvt/acc
				avvr = avvr/acc
				avvw = avvw/acc
				avvo = avvo/acc

				gr.append(avvg)
				lp.append(avvl)
				tc.append(avvt)
				ran.append(avvr)
				wss.append(avvw)
				uoo.append(avvo)

				weixx.append(wei)
				break




	print "..........................."

	for tms in range (15, 15, 1):
		print"current times", tms
		c = 0
		avvg = 0
		avvl = 0
		avvr = 0
		avvw = 0
		avvo = 0

		avvt = 0
		acc = 0
		while 1:
			status, grload, maxloadlp, rando, ws, uo, elap = allinone(numShard, numTrans, 10, tms)
			if status == 1:
				avvg = avvg + grload
				avvl = avvl + maxloadlp
				avvt = avvt + elap
				avvr = avvr + rando
				avvw = avvw + ws
				avvo = avvo + uo
				acc = acc + 1
			c = c + 1
			if c == Maxcount:
				avvg = avvg/acc
				avvl = avvl/acc
				avvt = avvt/acc
				avvr = avvr/acc
				avvw = avvw/acc
				avvo = avvo/acc

				gr.append(avvg)
				lp.append(avvl)
				tc.append(avvt)
				ran.append(avvr)
				wss.append(avvw)
				uoo.append(avvo)

				tmsxx.append(tms)
				break

	print "..........................."

	print gr

	print lp

	print ran

	print wss

	print uoo

	print weixx

	print tmsxx

	print tc


	gr = [3755, 4209, 4590, 5194, 5780, 6051, 6715, 7023, 7454, 8287]
	lp = [3596.0, 3969.25, 4409.0, 4769.8, 5348.5, 5714.0, 6270.2, 6625.6, 6940, 7517.0]
	ran = [4066, 4557, 5058, 5722, 6270, 6698, 7258, 7890, 8434, 8983]
	tmsxx = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	uoo = [3369.2, 3743.7249999999995, 4082.8250000000003, 4513.719999999999, 4907.25, 5205.1, 5735.1, 6028.2, 6340.5199999999995, 6785.375]

	tmsxx = [tmsxx[i]*6 for i in range(0, len(tmsxx))]
	gr = [ (gr[i]-uoo[i])/float(uoo[i]) for i in range(0,len(uoo))] 
	lp = [ (lp[i]-uoo[i])/float(uoo[i]) for i in range(0,len(uoo))] 
	ran = [ (ran[i]-uoo[i])/float(uoo[i]) for i in range(0,len(uoo))] 

	fig,ax = plt.subplots(1, 1, figsize = (50,20))

	line1 = ax.plot(tmsxx, gr, label='Greedy', color = 'red', marker = 'o', drawstyle='steps-mid', linewidth = 20, markersize = 80)
	ax.plot(tmsxx, gr, linestyle='--', color = 'grey', linewidth = 20)
	

	line2 = ax.plot(tmsxx, lp, label = '$\mathrm{LP}$', drawstyle = 'steps-mid', color = 'blue', linewidth = 20, marker = 'o', markersize = 80)
	ax.plot(tmsxx, lp,  linestyle='-.', color = 'grey', linewidth = 20)

	line3 = ax.plot(tmsxx, ran, label = 'Random', drawstyle = 'steps-mid', color = 'green', linewidth = 20, marker = 'X', markersize = 80)
	ax.plot(tmsxx, ran, linestyle=':', color = 'grey', linewidth = 20)

	# ax.grid(visible = True, linewidth = '20')
	# line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)


	ax.set_xticks(np.arange(24, 14*6, 12))
	ax.set_yticks(np.arange(0.05, 0.4, 0.08 	))

	ax.xaxis.set_tick_params( labelsize=200, pad = 25)
	ax.yaxis.set_tick_params( labelsize=200, pad = 25)

	ax.set_xlabel('$v_m$', fontsize = 200, labelpad = 10)
	ax.set_ylabel('$\epsilon$', fontsize = 200, rotation = 0, labelpad = 50)

	# ax.legend(loc="lower right", fontsize = 50)
	legend = ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.4), ncol = 3, columnspacing = 0.5, fontsize = 150)
	# legend.get_title().set_fontsize('50')

	ax.grid(visible = True, linewidth = '20', linestyle = ':')
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('simulvmax.pdf', bbox_inches = 'tight')




	# gr = [3789, 5635, 7393, 9194, 11070, 12884, 14742, 16667, 18363, 20414, 21834, 23958, 25936, 27907, 29651, 31645, 33175, 34922]
	# lp = [3602.7, 5331.3, 7051.7, 8828.777777777777, 10523.111111111111, 12279.6, 13837.888888888889, 15919.6, 17383.0, 19056.4, 20793.555555555555, 22661.0, 24311.3, 26355.777777777777, 28022.9, 29383.2, 31218.3, 32803.5]
	# ran = [4056, 5951, 7968, 10005, 11888, 13732, 15805, 17750, 19611, 21703, 23455, 25381, 27550, 29392, 31805, 33746, 35333, 37049]
	# weixx = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
	# uoo = [3421.5699999999997, 4998.4800000000005, 6599.770000000001, 8245.333333333334, 9859.233333333332, 11448.06, 13082.988888888889, 14770.429999999998, 16224.979999999996, 17783.879999999997, 19529.066666666666, 21141.510000000002, 22797.41, 24467.27777777778, 26170.170000000002, 27638.6, 29241.57, 30907.559999999998]
	# wss = [8163, 12156, 16395, 20466, 24658, 28737, 32677, 36987, 41088, 44960, 49663, 53444, 57611, 61801, 66095, 69692, 74526, 78366]

	# gr = [ (gr[i]-uoo[i])/float(uoo[i]) for i in range(0,len(uoo))] 
	# lp = [ (lp[i]-uoo[i])/float(uoo[i]) for i in range(0,len(uoo))] 
	# ran = [ (ran[i]-uoo[i])/float(uoo[i]) for i in range(0,len(uoo))] 

	# fig,ax = plt.subplots(1, 1, figsize = (40,20))

	# line1 = ax.plot(weixx, gr, drawstyle = 'steps-mid', label='Greedy', color='red', linewidth = 20, marker = 'o', markersize = 80)
	# ax.plot(weixx, gr, linestyle='--', color='grey', linewidth = 20)

	# line2 = ax.plot(weixx, lp, drawstyle = 'steps-mid', label = r'$\mathrm{LP}$', color = 'blue', linewidth = 20, marker = 'o', markersize = 80)
	# ax.plot(weixx, lp, linestyle='-.', color = 'grey', linewidth = 20)


	# line3 = ax.plot(weixx, ran, drawstyle = 'steps-mid', label = 'Random', color = 'green', linewidth = 20, marker = 'o', markersize = 80)
	# ax.plot(weixx, ran, linestyle=':', color = 'grey', linewidth = 20)

	# # line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# # line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)


	# ax.set_xticks(np.arange(10, 100, 20))
	# plt.gca().xaxis.set_major_formatter(FuncFormatter(changex))
	# ax.set_yticks(np.arange(0.05, 0.25, 0.05	))

	# ax.xaxis.set_tick_params( labelsize=200, pad = 25)
	# ax.yaxis.set_tick_params( labelsize = 200, pad = 25)

	# ax.set_xlabel(r'$v_{\mathrm{avg}} (\times$ 10)', fontsize = 200, labelpad = 10)
	# ax.set_ylabel('$\epsilon$', fontsize = 200, rotation = 0, labelpad = 50)

	# ax.grid(visible = True, linewidth = 10)

	# # ax.legend(loc="lower right", fontsize = 20)
	# legend = ax.legend(loc="upper center", bbox_to_anchor=(0.4, 1.4), ncol = 3, columnspacing = 0, fontsize = 150)
	# # plt.title('maximum load with respect to average confirmations', fontsize = 20)

	# plt.savefig('simulpra.pdf', bbox_inches = 'tight')

	# while 1:
	# 	avvg = 0
	# 	avvl = 0
	# 	avvt = 0
	# 	status, grload3, maxloadlp, elap = allinone()
	# if status == 1:
	# 	avvg = avvg + grload3
	# 	avvl = avvl + maxloadlp
	# 	avvt = avvt + elap
	# 	acc = acc + 1
	# if c >= Maxcount:
	# 	avvg = avvg/acc
	# 	avvl = avvl/acc
	# 	avvt = avvt/acc
	# 	break




	

	

	# getTrans(weights, numTrans, AverageN)

	# # totallp, maxlp = lpprog1(numShard, numTrans, weights)

	# # print("total lp, maxlp, all total"), totallp, " ", maxlp, sum(weights)

	# arraynono = [[0 for i in range(numTrans)] for j in range(numShard)]

	# timeb = time.time()
	# grload = greedy(weights, numShard, arraynono)
	# timea = time.time()

	# grload2 = greedywithcons(weights, numShard, arraynono)

	# arraynonono = [[0 for i in range(numTrans)] for j in range(numShard)]
	# grload3 = greedyonlyconstraints(weights, numShard, arraynonono)
	

	# print 'mmm', timea-timeb
	# weights.sort(reverse = True)
	# arrayo = [[0 for i in range(numTrans)] for j in range(numShard)]
	# grload1 = greedy(weights, numShard, arrayo)

	

	# print grload, "after sorting...", grload1, "after constraints....", grload2, "only constraints...", grload3

	# opb = grload/2

	# # print opb


	# total = sum(weights)

	# mid = (opb+grload)/2
	# lower = opb
	# upper = grload

	# # print mid

	
	# maxcount = 49
	# count = 0
	# telap = 0
	

	# # print (weights[1]**(numTrans*numShard))
	# totallp, maxloadlp, elap = lpprog1(numShard, numTrans, weights, grload)
	# telap = elap
	# # print("greedy result = "), (grload), "greedy total = ", total
	# # print("lp result = "), (maxloadlp), "lp total =", totallp
	
	
	# # while 1:
	# # 	# print mid
	# # 	totallp, maxloadlp, elap = lpprog1(numShard, numTrans, weights, mid)
	# # 	totallp = -totallp
	# # 	maxloadlp = -maxloadlp
	# # 	telap = telap + elap
		
	# # 	if totallp == total:
			
	# # 		upper = mid
	# # 		lower = lower
	# # 		mid = (upper + lower)/2
	# # 	elif totallp < total:
	# # 		lower = mid
	# # 		upper = upper
	# # 		mid = (lower + upper)/2
	# # 	if(totallp < total):
	# # 		print mid, grload, opb, totallp, total
	# # 		count = count + 1
	# # 	if(abs(totallp) - total > -0.1):
	# # 		break
	# # 	elif(count == maxcount):
	# # 		break
		

	# print("count "), count, "time needed", telap
	# print("greedy result = "), (grload), "greedy total = ", total
	# print("lp result = "), (maxloadlp), "lp total =", totallp, ", ", mid
	# print "done..."




	# print(" greedy done!")

