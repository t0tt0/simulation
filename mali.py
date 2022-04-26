from matplotlib import pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FuncFormatter


def changex(xti, position):
	return xti/int(10)

if __name__ == "__main__":



	total_width, n = 0.8, 2
	width = total_width*10 / n

	value = math.factorial(3000)
	value1 = math.factorial(300)
	# value1 = math.pow(value1, 10)
	for i in range (10):		
		value = value/(value1)
	valuestr = str(value)
	print (valuestr)
	print len(valuestr)


	malic = [ 20, 30, 40, 50, 60, 70, 80, 90]
	pyramid = [12.668342348629,	10.8333313208491,	9.80738984939576,	8.94425651991494,	8.31721254845134,	5.55136066972211,	3.60151799764446,	2.03291331157085]
	ours = [20.8343939222818,	19.2267473036362,	17.4996038466966,	18.330885987061,	13.6272119228487,	11.4081993331991,	7.05698305499006,	2.79749417647814]

	fig,ax = plt.subplots(1, 1, figsize = (40,20))
	ax.tick_params(direction='in', length=60, width=20,
                grid_alpha=0.5, bottom=False)


	line1 = ax.plot(malic, pyramid, drawstyle = 'steps-mid', label='Pyramid', color='red', linewidth = 20, marker = 'o', markersize = 80)
	ax.plot(malic, pyramid, linestyle = '--', color = 'grey', linewidth = 20)


	# for i in range (len(malic)):
	# 	malic[i] = malic[i] + width
	line2 = ax.plot(malic, ours, drawstyle = 'steps-mid', label = 'Silver', color = 'blue', linewidth = 20, marker = 'o', markersize = 80)
	ax.plot(malic, ours, linestyle = '-.', color = 'grey', linewidth = 20)
	# line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)
 

	ax.set_xticks(np.arange(20, 100, 10))
	ax.set_yticks(np.arange(0, 23, 5	))
	plt.gca().xaxis.set_major_formatter(FuncFormatter(changex))


	ax.xaxis.set_tick_params( labelsize=200, pad = 30)
	ax.yaxis.set_tick_params( labelsize=200, pad = 30)

	ax.set_xlabel(r'malicious%$(\times$ 10)', fontsize = 200, labelpad = 10)
	ax.set_ylabel('$\mathrm{TPS}$', fontsize = 200, rotation = 90, labelpad = 10)

	ax.grid(visible = True, linewidth = 20)

	# ax.legend(loc="upper right", fontsize = 20)
	legend = ax.legend(loc="upper center",  fontsize = 180, bbox_to_anchor=(0.4, 1.4), ncol = 2)
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('malicious.pdf', bbox_inches = 'tight')
