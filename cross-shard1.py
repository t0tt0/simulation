from matplotlib import pyplot as plt

if __name__ == "__main__":



	total_width, n = 0.8, 2
	width = total_width / n

	v_avg = [3, 5, 7, 9, 11, 13, 15, 17]
	pyramid = [1221,	1991,	2847,	3761,	4814,	5831,	6425,	7624]
	ours = [0,	0,	0,	0,	0,	0,	0,	0]

	fig,ax = plt.subplots(1, 1, figsize = (10,5))

	line1 = ax.plot(v_avg, pyramid, label='Pyramid', linewidth = 5, color='red')
	# for i in range (len(v_avg)):
	# 	v_avg[i] = v_avg[i] + width
	line2 = ax.plot(v_avg, ours, label = 'Ours', linewidth = 5, color = 'blue')
	# line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)


	# ax.set_xticks(np.arange(10, AverageN, 5))
	# ax.set_yticks(np.arange(3000, 80000, 	))

	ax.xaxis.set_tick_params( labelsize=20)
	ax.yaxis.set_tick_params( labelsize=20)

	ax.set_xlabel('$v_{\mathrm{avg}}$', fontsize = 30, labelpad = 20)
	ax.set_ylabel('#cross-shard transactions', fontsize = 30, rotation = 90, labelpad = 20)

	ax.legend(loc="upper left", fontsize = 20)

	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('crossshard1.eps', bbox_inches = 'tight')
