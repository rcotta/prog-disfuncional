import re

def solve_p2(matches):

	# ret - contagem de cartas de cada tipo
	ret = [1 for i in range(len(matches))]

	# para cada ponto na i-ésima carta ...
	for i in range(len(matches)):
		# incrementar a contagem das cartas i+1 até i+pontos ...
		for j in range(i + 1, i + matches[i] + 1):
			ret[j] += 1 * ret[i] # ... em # de unidades da carta estudada unidades
	
	return ret

def count_matches(infos):
	"""
	Retorna lista com contagem de itens coincidentes para cada uma das
	instâncias do jogo
	"""

	ret = []

	for info in infos:
		matches = sum([1 for number in info[0] if number in info[1]])
		ret.append(matches)

	return ret


with open("input/day_4.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]

	# tmp : 0 - card x, 1 - numeros da sorte, 2 - suas cartas
	tmp = [re.split(":|\|", line) for line in lines]

	# infos : list com [0] : list de inteiros com cartas, [1] : list de inteiros com numeros
	infos = [[list(map(int, re.findall("[0-9]+", row[1]))), list(map(int, re.findall("[0-9]+", row[2])))] for row in tmp]
	matches = count_matches(infos)

	for part in [1, 2]:

		if part == 1:
			# para cada instância do jogo, calcular pontuação e acumular em ans
			ans = sum([0 if n == 0 else 2 ** (n - 1) for n in matches])

		if part == 2:
			ans = sum(solve_p2(matches))

		
		print(f"Resposta (parte {part}) -> {ans}")
