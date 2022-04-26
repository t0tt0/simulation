from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":



	total_width, n = 0.8, 2
	width = total_width / n

	v_avg = [3, 5, 7, 9, 11, 13, 15, 17, 19]
	pyramid = [8.32478299871988,	5.85648218393811,	3.22658869223661,	3.25031732016269,	2.82206846056726,	2.06730624801475,	1.65851231445,	1.90656867572,	1.63877769596]
	ours = [20.7287161375482,	15.6256226139496,	11.8722318885869,	9.79551896385308,	6.70539441375935,	6.03861241419932,	5.16930642475047,	4.21596194458438,	3.7258979206]
	chainspace = [8.1926910299,	5.157622739,	4.3777490298,	5.8993089832,	2.9476153245,	3.1540041068,	3.6157925751,	2.6338769069,	3.1911764706]


	fig,ax = plt.subplots(1, 1, figsize = (40,20))
	ax.tick_params(direction='in', length=60, width=20,
                grid_alpha=0.5, bottom=False)


	line1 = ax.bar(v_avg, pyramid, label='Pyramid', width=width, color='red')
	for i in range (len(v_avg)):
		v_avg[i] = v_avg[i] + width
	line2 = ax.bar(v_avg, ours, label = 'Sliver', width=width, color = 'blue')
	for i in range (len(v_avg)):
		v_avg[i] = v_avg[i] + width
	line3 = ax.bar(v_avg, chainspace, label = 'ChainSpace', width=width, color = 'green')
	# line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)


	ax.set_xticks(np.arange(3, 21, 4))
	ax.set_yticks(np.arange(0, 23, 	5))

	ax.xaxis.set_tick_params( labelsize=200, pad = 25)
	ax.yaxis.set_tick_params( labelsize=200, pad = 25)

	ax.grid(axis = 'y', linewidth = 20)

	ax.set_xlabel('$v_{\mathrm{avg}}$', fontsize = 200, labelpad = 10)
	ax.set_ylabel('$\mathrm{TPS}$', fontsize = 200, rotation = 90, labelpad = 10)

	# ax.legend(loc="upper right", fontsize = 20)
	legend = ax.legend(loc="upper center",  fontsize = 100, bbox_to_anchor=(0.4, 1.4), ncol = 3)
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('tps11.pdf', bbox_inches = 'tight')
