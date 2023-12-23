import re

def get_adj_nums(coord, numbers):

	"""
	Retorna um set de tuplas, onde cada item é um número adjacente à coordenada
	coord (x, y), utilizando o formato (x, y, numero).
	
	A função não verifica se a coordenada é ou não símbolo.
	"""

	# busca adjacentes acima e abaixo
	nums = set()

	# observar que cada item de numbers tem o formato {((x1, x2), y): numero}
	# todos os números nas linhas acima ou abaixo (ab -> above_below) (adjacentes em relação a Y)...
	ab_nums = {k:v for k, v in numbers.items() if k[1] in [coord[1] - 1, coord[1] + 1]}
	# ... e deixar somente os números adjacentes em relação a X
	ab_nums = {k:v for k, v in ab_nums.items() if coord[0] in range(k[0][0] - 1, k[0][1] + 1 + 1)}

	# todos os números na mesma linha que começam em x+1 ou terminam em x-1
	lr_nums = {k:v for k,v in numbers.items() if k[1] == coord[1] and coord[0] in [k[0][1] + 1, k[0][0] - 1]}

	# retorna a união dos números adjacentes acima, abaixo e ao lado no formato (x, y, numero)
	return set([(k[0][0], k[1], v) for k,v in  (ab_nums | lr_nums).items()])


with open("input/day_3.input") as f:

	numbers = {}
	symbols = {}


	# leitura do arquivo para as estruturas numbers e symbols
	lines = [line.strip() for line in f.readlines()]

	for y in range(len(lines)):

		line = lines[y]

		# guarda números em um dict no formato {((x1, x2), y): number}
		matches = re.finditer("[0-9]+", line)
		for m in matches:
			v_i = int(m.group())
			numbers[((m.span()[0], m.span()[1] - 1), y)] = v_i

		# guarda os símbolos em um dict no formato {(x, y): symbol}
		for x in range(len(line)):
			if line[x] not in "0123456789.":
				symbols[(x, y)] = line[x]

	adj = {}
	for coord, symbol in symbols.items():
		adj[coord] = get_adj_nums(coord, numbers)

	for part in [1, 2]:

		ans = None

		# soma todos os números adjacentes a um símbolo
		if part == 1:
			ans_items = set([item for row in adj.values() for item in row])
			ans = sum([item[2] for item in ans_items])

		# considerando somente símbolos *, busca os adjacentes, filtra por quem
		# tem exatamente dois itens adjacentes, e realiza a soma
		if part == 2:
			gear_items = [list(v) for k,v in adj.items() if len(v) == 2 and k in [c for c, v in symbols.items() if v == '*']]
			ans = sum([item[0][2] * item[1][2] for item in gear_items])

		print(f"Resposta (parte {part}) -> {ans}")
