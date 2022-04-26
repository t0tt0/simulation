import time

import random
import math
from scipy.special import comb, perm
from matplotlib import pyplot as plt
import numpy as np

def getj(va):
	re = 1
	for i in range(1, va, 1):
		re = re*i 
	return re

if __name__ == '__main__':

	p = []

	x = 0
	m = []

	for f in range (10, 90, 1):
		fp = float(f)/100
		m.append(f)
		# print fp
		N = 100
		for i in range (int(fp*N), N, 1):
			x = x + float(pow(fp, i)*pow(1-fp, N)*comb(N, i))

		p.append(x)

	fig,ax = plt.subplots(1, 1, figsize = (10,5))

	line = ax.plot(m, p, label='Failure Probability', linestyle='--', color='red', linewidth = 5)
	


	# ax.set_xticks(np.arange(10, 90, 10))
	# ax.set_yticks(np.arange(3000, 80000, 	))

	ax.xaxis.set_tick_params( labelsize=20)
	ax.yaxis.set_tick_params( labelsize=20)

	# ax.set_xlabel('average confirmations per $T$', fontsize = 30, labelpad = 20)
	ax.set_ylabel('Failure Probability', fontsize = 30, rotation = 90, labelpad = 20)

	# ax.legend(loc="lower right")

	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('secu.pdf', bbox_inches = 'tight')

		

	
