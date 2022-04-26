from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":



	# total_width, n = 0.8, 4
	# width = total_width / n
	total_width, n = 0.8, 3
	width = total_width / n

	s = [3, 4, 5, 6, 7, 8, 9]
	pyramid3 = [29.2644757433,	24.4946808511,	31.0423452769,	39.6701030928,	46.8586052463,	53.2478632479,	58.1618224666]
	ours3 = [59.8528209321,	78.2809224319,	97.8865979381,	117.539432177,	133.879003559,	148.363636364,	172.378752887]
	chainspace3 = [20.2644757433,	20.4946808511,	21.0423452769,	23.6701030928,	28.8586052463,	25.2478632479,	22.1618224666]

	# pyramid9 = [26.4273275285,	21.7262797173,	27.5343047107,	33.8877192982,	39.3601347085,	48.7035633055,	55.4713656388]
	# ours9 = [58.3201638865,	74.9465648855,	97.1604305484,	111.574178935,	124.959568733,	150.854251012,	163.423580786]

	fig,ax = plt.subplots(1, 1, figsize = (55,20))

	ax.tick_params(direction='in', length=60, width=20,
                grid_alpha=0.5, bottom=False)


	for i in range (len(s)):
		s[i] = s[i] - width*2
	line1 = ax.bar(s, pyramid3, label='Pyramid', width=width)
	for i in range (len(s)):
		s[i] = s[i] + width
	line2 = ax.bar(s, ours3, label = 'Sliver', width=width)
	for i in range (len(s)):
		s[i] = s[i] + width
	line3 = ax.bar(s, chainspace3, label = 'ChainSpace', width=width)
	# for i in range (len(s)):
	# 	s[i] = s[i] + width
	# line3 = ax.bar(s, ours9, label = 'Silver, $v_{\mathrm{avg}}=9$', width=width)
	# line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)


	ax.set_xticks(np.arange(3, 10, 1))
	ax.set_yticks(np.arange(0, 200, 40))

	ax.xaxis.set_tick_params( labelsize=200, pad = 25)
	ax.yaxis.set_tick_params( labelsize=200, pad = 25)

	ax.set_xlabel('#shards', fontsize = 200, labelpad = 10)
	ax.set_ylabel('$\mathrm{TPS}_w$', fontsize = 200, rotation = 90, labelpad = 10)

	ax.grid(axis = 'y', linewidth = 20)

	# ax.legend(loc="upper left", fontsize = 50)
	# #legend = ax.legend(loc="upper center",  fontsize = 320, bbox_to_anchor=(0.45, 1.6), ncol = 2)
	legend = ax.legend(loc="upper center",  fontsize = 150, bbox_to_anchor=(0.5, 1.7), ncol = 3, columnspacing = 0.1, title = '$v_{\mathrm{avg}}$ = 3')
	legend.get_title().set_fontsize('200')
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('tpsw22.pdf', bbox_inches = 'tight')
