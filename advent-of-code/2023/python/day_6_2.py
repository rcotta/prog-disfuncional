import numpy as np
import re
import math

with open("input/day_6.input", "r") as f:

	lines = [line.replace(" ", "").strip() for line in f.readlines()]
	time = [int(v) for v in re.findall("[0-9]+", lines[0])].pop()
	record = [int(v) for v in re.findall("[0-9]+", lines[1])].pop()

	# A equação que nos dá as distâncias percorridas é: (P=tempo pressionado) => dist = P * (time - P)
	# Realizando as manipulações chegamos em => -P*P + P*time - dist = 0; equação de grau 2 com concavidade para cima,
	# ou seja, todas as soluções positivas estarão entre as raízes da equação.

	# Nossa resposta é a contagem de números inteiros entre essas raízes ...
	# Podemos resolver a equação com auxílio do Numpy.

	poli = np.polynomial.Polynomial(coef=(-record, time, -1)) # coeficientes: c, b, a (nesta ordem)
	roots = poli.roots()
	ans = math.ceil(roots[1])- math.ceil(roots[0])

	print(f"Resposta -> {ans}")