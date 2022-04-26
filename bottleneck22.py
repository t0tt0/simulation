from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter


def changex(xti, position):
	return int(xti/10)

if __name__ == "__main__":



	total_width, n = 0.8, 3
	width = total_width / n

	numb = [20, 40, 60, 80, 100, 120, 140, 160, 180]
	tps3 = [5.9,	14.5,	15.8,	16,	19.6,	24.5,	20.1,	22.7,	20.7]
	tps7 = [2.9,	8.6,	13.2,	12.1,	16.9,	22.1,	20.1,	23.7,	20.9]
	tps9 = [2.2,	6.9,	7.8,	11.3,	12,	15,	15.4,	18.2,	20.3]

	fig,ax = plt.subplots(1, 1, figsize = (55,20))
	ax.tick_params(direction='in', length=60, width=20,
                grid_alpha=0.5, bottom=False)

	for i in range (len(numb)):
		numb[i] = numb[i] - width*20
	line1 = ax.bar(numb, tps3, label= '3', width=width*20, color='red')
	for i in range (len(numb)):
		numb[i] = numb[i] + width*20
	line2 = ax.bar(numb, tps7, label = '7', width=width*20, color = 'blue')
	for i in range (len(numb)):
		numb[i] = numb[i] + width*20
	line3 = ax.bar(numb, tps9, label = '9', width=width*20, color = 'green')
	# line4 = ax.plot(weixx, wss, label = 'Worst', linestyle='-.', color = 'blue', linewidth = 5)
	# line5 = ax.plot(weixx, uoo, label = 'Average Load', linestyle='-.', color = 'blue', linewidth = 5)

	numb = [20, 40, 60, 80, 100, 120, 140, 160, 180]
	ax.set_xticks(np.asarray(numb))
	ax.set_yticks(np.arange(1, 25, 5))
	plt.gca().xaxis.set_major_formatter(FuncFormatter(changex))


	ax.xaxis.set_tick_params( labelsize=200, pad = 25)
	ax.yaxis.set_tick_params( labelsize=200, pad = 25)

	ax.set_xlabel(r'$\mathrm{TPS}_w (\times$ 10)', fontsize = 200, labelpad = 10)
	ax.set_ylabel('$\mathrm{TPS}$', fontsize = 200, rotation = 90, labelpad = 10)

	ax.grid(axis = 'y', linewidth = 20)

	legend = ax.legend(loc="upper center",  fontsize = 200, bbox_to_anchor=(0.5, 1.7), ncol = 3, columnspacing = 0.9, title = '$v_{\mathrm{avg}}$')
	legend.get_title().set_fontsize('200')
	# plt.title('maximum load with respect to average confirmations', fontsize = 20)

	plt.savefig('bottleneck22.pdf', bbox_inches = 'tight')
