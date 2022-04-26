from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":



	total_width, n = 0.8, 4
	width = total_width / n

	s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	opt3 = [3.1,	7.2,	10.1,	11.2,	16.7,	19.2,	21,	20.3,	19.3]
	ours3 = [2.75253173221186,	5.41290300475001,	8.16703895548404,	10.8070122867069,	13.13126756168,	14.4338935840762,	15.1566328706029,	15.7524376259456,	16.1867301973863]
	opt9 = [1.7,	5.2,	9.2,	9.6,	10,	13,	14.3,	15.6,	19.96]
	ours9 = [1.10423337658221,	4.23312888234195,	6.32509395655239,	8.4055828644552,	11.4806299936339,	12.6887223036358,	13.2150771006007,	15.0234293126059,	15.5741056125985]

	fig,ax = plt.subplots(1, 1, figsize = (120,40))
	ax.tick_params(direction='in', length=60, width=20,
                grid_alpha=0.5, bottom=False)

	for i in range (len(s)):
		s[i] = s[i] - width*2
	line1 = ax.bar(s, opt3, label='AdB, $v_{\mathrm{avg}}=7$', width=width)
	for i in range (len(s)):
		s[i] = s[i] + width
	line2 = ax.bar(s, ours3, label = 'Silver, $v_{\mathrm{avg}}=7$', width=width)
	for i in range (len(s)):
		s[i] = s[i] + width
	line3 = ax.bar(s, opt9, label = 'AdB, $v_{\mathrm{avg}}=9$', width=width)
	for i in range (len(s)):
		s[i] = s[i] + width
	line3 = ax.bar(s, ours9, label = 'Silver, $v_{\mathrm{avg}}=9$', width=width)
	# line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)


	ax.set_xticks(np.arange(1, 10, 1))
	ax.set_yticks(np.arange(0, 23, 5	))

	ax.xaxis.set_tick_params( labelsize=450, pad = 100)
	ax.yaxis.set_tick_params( labelsize=450, pad = 100)

	ax.grid(axis = 'y', linewidth = 40)

	ax.set_xlabel('#shards, #transactions per block', fontsize = 450, labelpad = 10)
	ax.set_ylabel('$\mathrm{TPS}$', fontsize = 450, rotation = 90, labelpad = 10)

	# ax.legend(loc="upper right", fontsize = 20)
	legend = ax.legend(loc="upper center",  fontsize = 350, bbox_to_anchor=(0.45, 1.67), ncol = 2)
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('tpsc.pdf', bbox_inches = 'tight')
