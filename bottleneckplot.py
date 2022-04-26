from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":



	total_width, n = 0.8, 3
	width = total_width / n

	v_avg = [3, 4, 5, 6, 7, 8, 9, 10]
	tps1 = [5.8, 3.2, 2.8, 1.9, 2.5, 1.9, 1.7, 1.3]
	tps2 = [13, 7.6, 5.8, 2.6, 4.1, 3.2, 3.6, 3]
	tps3 = [18.6, 10.7, 8.7, 4, 6.2, 4.3, 4.6, 3.6]

	fig,ax = plt.subplots(1, 1, figsize = (40,20), dpi = 300)
	ax.tick_params(direction='in', length=60, width=20,
                grid_alpha=0.5, bottom=False)

	for i in range (len(v_avg)):
		v_avg[i] = v_avg[i] - width
	line1 = ax.bar(v_avg, tps1, label='20', width=width, color='red')
	for i in range (len(v_avg)):
		v_avg[i] = v_avg[i] + width
	line2 = ax.bar(v_avg, tps2, label = '40', width=width, color = 'blue')
	for i in range (len(v_avg)):
		v_avg[i] = v_avg[i] + width
	line3 = ax.bar(v_avg, tps3, label = '60', width=width, color = 'green')
	# line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)

	v_avg = [3, 4, 5, 6, 7, 8, 9, 10]
	ax.set_xticks(np.arange(3, 11, 1))
	ax.set_yticks(np.arange(1, 20, 4))

	ax.xaxis.set_tick_params( labelsize=200, pad = 25)
	ax.yaxis.set_tick_params( labelsize=200, pad = 25)

	ax.set_xlabel('$v_{\mathrm{avg}}$', fontsize = 200, labelpad = 10)
	ax.set_ylabel('$\mathrm{TPS}$', fontsize = 200, rotation = 90, labelpad = 10)

	ax.grid(axis = 'y', linewidth = 20, linestyle = ":")

	legend = ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.6), ncol = 3, columnspacing = 0.9,  title = '$\mathrm{TPS}_w$', fontsize = 150)
	legend.get_title().set_fontsize('200')
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('bottleneck1.pdf', bbox_inches = 'tight', dpi = 300)
