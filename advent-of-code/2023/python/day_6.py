import numpy as np
import math


def solve_instance(record, time):

	"""
	Retorna a quantidade de respostas vencedoras dado record e time.
	
	A equação que nos dá as distâncias percorridas é: (P=tempo pressionado) => dist = P * (time - P)
	Realizando as manipulações chegamos em => -P*P + P*time - dist = 0; equação de grau 2 com concavidade para cima,
	ou seja, todas as soluções positivas estarão entre as raízes da equação.
	Nossa resposta é a contagem de números inteiros entre essas raízes ...
	Podemos resolver a equação com auxílio do Numpy.
	"""

	poli = np.polynomial.Polynomial(coef=(-record, time, -1)) # coeficientes: c, b, a (nesta ordem)
	roots = poli.roots()
	return (math.ceil(roots[1])- math.ceil(roots[0]))


with open("input/day_6.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]
	times = [int(v) for v in lines[0].split(":")[1].split(" ") if v != ""]
	records = [int(v) for v in lines[1].split(":")[1].split(" ") if v != ""]


	for part in [1, 2]:

		ans = None

		if part == 1:
			wins = []
			for i in range(len(times)):
				wins.append(solve_instance(records[i], times[i]))
			ans = np.prod(wins)

		if part == 2:
			time_s, record_s = "", ""
			for time in times: time_s = time_s + str(time)
			for record in records: record_s = record_s + str(record)
			ans = solve_instance(int(record_s), int(time_s))

		print(f"Resposta (parte {part}) -> {ans}")
	
