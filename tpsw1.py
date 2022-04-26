from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":



	# total_width, n = 0.8, 2
	# width = total_width / n

	total_width, n = 0.8, 3
	width = total_width / n

	v_avg = [3, 5, 7, 9, 11, 13, 15, 17, 19]
	pyramid = [28.6290739783,	28.1239157373,	28.2904689864,	27.137366548,	26.432194792,	24.5511782695,	26.5525040388,	25.6872768013,	25.7722815564]
	chainspace = [20.6290739783,	22.1239157373,	21.2904689864,	23.137366548,	25.432194792,	20.5511782695,	19.5525040388,	18.6872768013,	21.7722815564]
	ours = [92.1926910299,	97.157622739,	96.3777490298,	93.8993089832,	92.9476153245,	95.1540041068,	95.6157925751,	95.6338769069,	94.1911764706]

	fig,ax = plt.subplots(1, 1, figsize = (55,20))


	ax.tick_params(direction='in', length=60, width=20,
                grid_alpha=0.5, bottom=False)

	# fig.tick_params(top=True,bottom=True,left=True,right=True)
	# fig.tick_params(direction='in')

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
	ax.set_yticks(np.arange(0, 125, 25	))


	ax.grid(axis = 'y', linewidth = 20)

	ax.xaxis.set_tick_params( labelsize=200, pad = 25)
	ax.yaxis.set_tick_params( labelsize=200, pad = 25)

	ax.set_xlabel('$v_{\mathrm{avg}}$', fontsize = 200, labelpad = 10)
	ax.set_ylabel('$\mathrm{TPS}_w$', fontsize = 200, rotation = 90, labelpad = 10)

	# ax.legend(loc="upper right", fontsize = 20)
	legend = ax.legend(loc="upper center",  fontsize = 150, bbox_to_anchor=(0.5, 1.3), ncol = 3, columnspacing = 1)
	# legend.get_title().set_fontsize('65')
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('tpsw11.pdf', bbox_inches = 'tight')
