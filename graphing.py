import math
import numpy as np
from numpy import log as ln
import matplotlib.pyplot as plt
import scipy.optimize


def nernst(h):
	y2_list = []

	s1 = 0.799  # standard potential of first element
	s2 = -2.37  # standard potential of second element
	e0 = s1 - s2  # standard potential
	z = 2  # ion
	r = 1

	for element in h:
		y_list = []
		print(element)
		for i in range(5):
			o = element
			E = e0 - ((8.314 * 298.15) / (z * 96485)) * ln(o / r)
			E = E + np.random.normal(-0.005, 0.005)
			y_list.append(E)
		print(y_list)
		print(sum(y_list))
		y2_list.append(sum(y_list) / 5)
	print(y2_list)
	return(h, y2_list)


def plotgraph(M, y):
	plt.figure()
	plt.rcParams['font.sans-serif'] = 'helvetica'
	plt.title("The Reduction Potential (in Volts) of a Magnesium-Silver Voltaic Cell System vs.\n The Natural Logarithm of the Molar Concentration of Magnesium Nitrate Solution", pad=20, ha='center')
	plt.xlabel("ln([Mg2+]) (M)", labelpad=10)
	plt.ylabel("Ecell (V)", labelpad=10)
	plt.xlim([-10, 1.5])
	plt.ylim([3.15, 3.3])
	M = ln(M)

	m, b = np.polyfit(M, y, 1)
	plt.plot(M, m * M + b, 'g')
	best = "line of best fit: " + str(round(m, 4)) + "x " + "+ " + str(round(b, 4))
	plt.text(-2, 3.28, best, c='g')

	correlation_matrix = np.corrcoef(M, y)
	correlation_xy = correlation_matrix[0, 1]
	r_squared = correlation_xy**2
	rrr = "R^2 value = " + str(r_squared)
	plt.text(-2, 3.275, rrr)

	Mr = [round(M[i], 5) for i in range(len(M))]
	yr = [round(y[i], 5) for i in range(len(y))]

	for ij in zip(Mr, yr):
		plt.annotate('(%s, %s)' %ij, xy=ij, xytext=(10, 10), textcoords='offset points', c='b')

	plt.scatter(M, y, c='b')
	plt.grid(linestyle='-', linewidth=0.5)
	plt.show()


def func(x, a, b, c):
	return a * np.exp(-b * x) + c


def plotgraphex(M, y):
	plt.figure()
	plt.rcParams['font.sans-serif'] = 'helvetica'
	plt.title("The Reduction Potential (in Volts) of a Magnesium-Silver Voltaic Cell System vs.\n The Molar Concentration of Magnesium Nitrate Solution", pad=20, ha='center')
	plt.xlabel("[Mg2+] (M)", labelpad=10)
	plt.ylabel("Ecell (V)", labelpad=10)
	plt.xlim([-0.1, 1.2])
	plt.ylim([3.15, 3.3])

	Mr = [round(M[i], 5) for i in range(len(M))]
	yr = [round(y[i], 5) for i in range(len(y))]

	for ij in zip(Mr, yr):
		plt.annotate('(%s, %s)' %ij, xy=ij, xytext=(10, 10), textcoords='offset points', c='b')

	plt.scatter(M, y, c='b')
	plt.grid(linestyle='-', linewidth=0.5)
	plt.show()


a = [0.0001, 0.001, 0.01, 0.1, 1]
M, y = nernst(a)

print(M, y)
plotgraph(M, y)
plotgraphex(M, y)
