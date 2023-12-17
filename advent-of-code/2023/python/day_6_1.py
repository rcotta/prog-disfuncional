import numpy as np
import math

with open("input/day_6.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]
	times = [int(v) for v in lines[0].split(":")[1].split(" ") if v != ""]
	records = [int(v) for v in lines[1].split(":")[1].split(" ") if v != ""]

	# A equação que nos dá as distâncias percorridas é: (P=tempo pressionado) => dist = P * (time - P)
	# Realizando as manipulações chegamos em => -P*P + P*time - dist = 0; equação de grau 2 com concavidade para cima,
	# ou seja, todas as soluções positivas estarão entre as raízes da equação.

	# Nossa resposta é a contagem de números inteiros entre essas raízes ...
	# Podemos resolver a equação com auxílio do Numpy.

	wins = []
	for i in range(len(times)):
		time = times[i]
		record = records[i]
		poli = np.polynomial.Polynomial(coef=(-record, time, -1)) # coeficientes: c, b, a (nesta ordem)
		roots = poli.roots()
		wins.append(math.ceil(roots[1])- math.ceil(roots[0]))

	ans = np.prod(wins)
	print(f"Resposta -> {ans}")
	

''' ### ABORDAGEM ORIGINAL ###

	won = [0 for i in range(len(times))]

	for i in range(len(times)):
		
		for t in range(times[i] + 1):
			won[i] += 1 if (t * (times[i] - t)) > records[i] else 0

	ans = f"{np.prod(won)}"
	print(f"Resposta -> {ans}")

### '''