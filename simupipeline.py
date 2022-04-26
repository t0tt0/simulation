#!/usr/bin/python3

import threading
import time

# import numpy as np
# # import scipy.optimize as op
import random
# from inspect import getmembers
import pulp as pulp
# import math
# import time
# from matplotlib import pyplot as plt

semaphore = threading.Semaphore(0)
semaphore1 = threading.Semaphore(0)
semaphore2 = threading.Semaphore(0)
semaphore3 = threading.Semaphore(0)
# semaphore = []
threadLock = threading.Lock()
threads = []
# 
# global pointer

class regThread (threading.Thread):
    def __init__(self, threadID, name, numTrans, delay, numBlock, ShardId, weights, res): #numshard: blocksize
    	# pointer = -1
    	threading.Thread.__init__(self)
    	self.threadID = threadID
    	self.name = name
    	self.numTrans = numTrans
    	self.delay = delay
    	
    	self.numBlock = numBlock
    	self.ShardId = ShardId
    	self.weights = weights
    	self.res = res
        # self.semaphore = semaphore
    def run(self):
        print ("starting regChain： " + self.name)

        x = int(self.numTrans/numBlock)
        for i in range (x):
        	if int(res[self.ShardId][i]) == 0:
        		continue
        	time.sleep(self.delay)
        	
        	# print (numBlock)
        	# rsa = int(self.numst/self.numTrans)
        	rda = int(((self.weights)[i]-1)/2)
        	rsa = (self.weights)[i] - 1 - rda
        	# print (rsa)
        	# print (rsa)
        	# print ("hh")
        	for j in range (numBlock*rsa):
        		threadLock.acquire()
	        	semaphore.release()
	        	threadLock.release()
	        	# print ("r " + str(i) + " " + str(self.ShardId))
        	
        for i in range (x):
        	# print (int(res[self.ShardId][i]))
        	if int(res[self.ShardId][i]) == 0:
        		# print (",,,,,,,,,,,,,,,")
        		continue
        	# rda = int(((self.weights)[i]-1)/2)
        	# rsa = (self.weights)[i] - 1 - rda

        	for j in range ((self.weights)[i] - 1 - int(((self.weights)[i]-1)/2)):
        		# threadLock.acquire()
        		semaphore1.acquire()
        		ic = random.random()
        		ic = 1
        		if ic >= 0.7:
        			time.sleep(self.delay)
        		else:
        			time.sleep(self.delay*2)
        		# time.sleep(self.delay)
        		semaphore2.release()
        		# print ("c1 " + str(i) + "semaphore1 "+str(semaphore1._value) + " "+ self.name)
        		# threadLock.release()

        # print ("test.....")
        for i in range (x):
        	# print("test")
        	if int(res[self.ShardId][i]) == 0:
        		continue
        	# print("test...")
        	rda = int(((self.weights)[i]-1)/2)
        	rsa = (self.weights)[i] - 1 - rda

        	for j in range (int(((self.weights)[i]-1)/2)):
        		threadLock.acquire()
        		semaphore3.acquire()
        		threadLock.release()
        		ic = random.random()
        		ic = 1
        		if ic > 0.7:
        			time.sleep(self.delay)
        		else:
        			time.sleep(self.delay*3)
        		# time.sleep(self.delay)
        		print ("c2 " + str(i))

        		
        # xx = int(self.numst/numShard)
        # for i in range (xx):
        # 	threadLock.acquire()
        # 	for j in range (numShard):
        # 		semaphore1.acquire()
        # 	threadLock.release()

        # 	time.sleep(self.delay)

        # 	# print ("c1", str(i))

        # 	threadLock.acquire()
        # 	for j in range (numShard):
	       #  	semaphore2.release()
        # 	threadLock.release()

        # xxx = int(self.numdt/numShard)
        # for i in range (xxx):
        # 	threadLock.acquire()
        # 	for j in range (numShard):
	       #  	semaphore3.acquire()
        # 	threadLock.release()
        # 	time.sleep(self.delay)
        # 	print ("c2 " + str(i))

        print(semaphore3._value)
        print(semaphore2._value)
        print(semaphore1._value)
        print(semaphore._value)

class sourceThread (threading.Thread):
    def __init__(self, threadID, name, numTrans, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.numTrans = numTrans
        self.delay = delay/10
    def run(self):
        print ("starting sourceChain： " + str(self.numTrans))
        for i in range (self.numTrans):
        	semaphore.acquire()
        	time.sleep(self.delay)
        	# print ("s1 "+ str(i))	
        	semaphore1.release()


        	# print_confirmedS(self.name, self.delay, i)

        # threadLock.acquire()
        # print_confirmedS(self.name, delay, numTrans)
        # threadLock.release()

    # def print_confirmedS(threadName, delay, i):
  

class dstThread (threading.Thread):
	def __init__(self, threadID, name, numTrans, delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.numTrans = numTrans
		self.delay = delay/10
        # self.semaphore = semaphore

	def run(self):
		print ("starting dstChain： " + self.name)
		for i in range (self.numTrans):
			semaphore2.acquire()
			time.sleep(self.delay)
			# print ("d2 " + str(i))
			semaphore3.release()     
		print (semaphore3._value)

def lpprog1(numShard, numTrans, weights, res):
	# print(SSize)
	
	for i in range (len(weights)):
		weights[i] = weights[i]

	variables = [[pulp.LpVariable("x%d,%d"%(i, j) ,lowBound=0, cat='Continuous') for j in range(numTrans)] for i in range(numShard)]

	# print("variables done")

	
	

	prob = pulp.LpProblem('LP2', pulp.LpMinimize)

	
	c = sum(weights)/float(numShard)
	w = sum(weights)

	

	prob += pulp.lpSum( (variables[int(i/numTrans)][int(i%numTrans)])*(weights[int(i%numTrans)]*(2**(weights[int(i%numTrans)])))*(numTrans - int(i%numTrans) - 1) for i in range(numShard*numTrans) )
	
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
		res[int(ind/numTrans)][int(ind%numTrans)] = var.varValue
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

	print ("calculated objective is"+ str( pulp.value(prob.objective)) + "testva is = " + str( testva))

	return total, max(loads), elap

def getTrans(weights, numTrans, AverageN, tms):
	sd = (tms - 1)*AverageN/3
	for i in range (numTrans):
		w = int(random.gauss(AverageN, sd))
		if w < 3:
			w = int(3)
		if w%2 == 0:
			w = w-1
		# print w
		weights.append(w)

if __name__ == '__main__':

	
	numBlock = 1
	fp = 0
	numShard = int(1*(1-fp))
	if numShard == 0:
		numShard = 1

	numTrans = 20*numShard
	vavg = 6
	# dTrans = numTrans*(int((vavg-1)/int(2)))
	# sTrans = (vavg*numTrans - dTrans)-numTrans



	# sTrans = numTrans*(int((vavg-1)/int(2)))
	# dTrans = (vavg*numTrans - sTrans)-numTrans

	weights = []
	tms = 4
	# numShard = 10

	# getTrans(weights, numTrans, vavg, tms)

	weights = [9 for i in range(numTrans)] 

	res = [[0 for i in range(numTrans)] for j in range(numShard)]
	# res = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
	
	# weights = [5, 5, 3, 3, 7, 7, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 3, 5, 3, 3, 5, 3, 5, 3, 3, 3, 9, 3, 5, 11, 3, 3, 3, 7, 3, 3, 3, 7, 3, 3, 3, 3, 3, 3, 5, 5, 3, 3, 3, 5, 5, 3, 3, 3, 7, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 3, 3, 3, 9, 5, 3, 3, 7, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
	totallp, maxloadlp, elap = lpprog1(int(numShard), int(numTrans), (weights), res)
	


	# print (5%2)

	

	# print (weights)

	sumvt = sum(weights)
	sTrans = int((sumvt -numTrans)/2)
	dTrans = int((sumvt -numTrans)/2)

	print (sTrans)
	print (dTrans)

	for t in range(numShard):
		threads.append(regThread(t, "regThread-"+str(t), numTrans, 0.05, numBlock, t, weights, res))

	# thread1 = regThread(1, "regThread-1", numTrans, 0.05, numBlock, ShardId, weights, res)


	thread2 = sourceThread(2, "sourceThread-2", sTrans, 0.05)
	thread3 = dstThread(3, "dstThread-3", dTrans, 0.05)

	# threads.append(thread1)
	threads.append(thread2)
	threads.append(thread3)



	stime = time.time()


	for t in threads:
		t.start()
	# thread1.start()
	# thread2.start()
	# thread3.start()



	for t in threads:
		t.join()
		# print("exiting")

	etime = time.time()

	print (numTrans/(etime -stime))

	print("exit")

