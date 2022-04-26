from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":



	total_width, n = 0.8, 3
	width = total_width / n

	s = [3, 4, 5, 6, 7, 8, 9]
	pyramid3 = [6.15517503886145,	9.46964891574847,	10.0827014873671,	13.3604483421097,	14.7006658070754,	16.1190334187254,	15.5314392571815]
	ours3 = [15.988441440144,	18.7854397464464,	21.1566238710464,	20.8037124075737,	21.9768307544573,	21.8677392239522,	21.6343644759979]
	chainspace3 = [6.15517503886145,	10.46964891574847,	9.0827014873671,	10.3604483421097,	13.7006658070754,	15.1190334187254,	13.5314392571815]
	# pyramid9 = [2.01209510600296,	2.24707771820779,	2.60014414235326,	3.72163995523575,	4.2835944992747,	4.09367225693411,	5.37893379899218]
	# ours9 = [5.51405212307829,	7.26792367680656,	9.0082606678834,	9.72293610924598,	11.8456100472183,	12.6630836445836,	13.1498692711177]

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
	ax.set_yticks(np.arange(0, 23, 5	))

	ax.xaxis.set_tick_params( labelsize=200, pad = 10)
	ax.yaxis.set_tick_params( labelsize=200, pad = 10)

	ax.set_xlabel('#shards', fontsize = 200, labelpad = 10)
	ax.set_ylabel('$\mathrm{TPS}$', fontsize = 200, rotation = 90, labelpad = 10)

	ax.grid(axis = 'y', linewidth = 40)

	# ax.legend(loc="upper left", fontsize = 65)
	# #legend = ax.legend(loc="upper center",  fontsize = 200, bbox_to_anchor=(0.45, 1.6), ncol = 3)
	legend = ax.legend(loc="upper center",  fontsize = 150, bbox_to_anchor=(0.5, 1.7), ncol = 3, columnspacing = 0.1, title = '$v_{\mathrm{avg}}$ = 3')
	legend.get_title().set_fontsize('200')
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('tps22.pdf', bbox_inches = 'tight')
