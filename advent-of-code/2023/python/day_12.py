import time

# variável que guarda resultados intermediários
cache = None

def solve(s: str, answer: list, partial: list, cur_reading: int, i: int) -> int:

	"""
	Verifica se o arranjo proposta em s é compatível com a solução esperada em answer.
	Retorna 1 caso positivo, ou 0 caso contrário.

	s: str
		hipótese com ?'s, .'s e #'s sendo validada
	answer: list
		resposta esperada, informada no input do problema
	partial: list
		resposta parcial (lista com tamanhos dos blocos de # em s até a posição i)
	cur_reading: int
		tamanho do bloco sendo lido no momento (tamanho do bloco de # desde o início de
		s ou do último ponto até i)
	i: int
		posição em que a inspeção de s está ocorrendo no momento
	"""

	# block reading
	c = None if i == len(s) else s[i]
	ret = 0
	key = None

	if c == '?':
		ret += solve(s[:i] + '.' + s[i+1:], answer, partial, cur_reading, i)
		ret += solve(s[:i] + '#' + s[i+1:], answer, partial, cur_reading, i)

	else:

		if cur_reading > 0:
			if c == '#':
				cur_reading += 1
			elif c == '.' or c == None:
				partial = partial + [cur_reading]
				cur_reading = 0

		elif cur_reading == 0 and c == '#':
			cur_reading = 1

		# cache
		key = (tuple(partial), cur_reading, i)
		if key in cache: return cache[key]
	
		# condição de parada
		if len(s) == i:
			ret = 1 if answer == partial else 0
			cache[key] = ret
		
		else:
			skip = False
			
			if c == '.':
				len_partial = len(partial)
				if partial != answer[:len_partial]:
					skip = True

			if cur_reading:
				len_partial = len(partial)
				if len_partial < len(answer) and answer[len_partial] < cur_reading:
					skip = True
			
			if skip: ret = 0
			else: ret = solve(s, answer, partial, cur_reading, i + 1)
			cache[key] = ret
				
	return ret

with open("input/day_12.input", "r") as f:

	infos = [line.strip().split(" ") for line in f.readlines()]
	instances = [(info[0], list(map(int, info[1].split(",")))) for info in infos]

	# otimização: substituindo ".." por ".", pois a quantidade de "." entre blocos não tem influência na resposta
	for instance in instances:
		while ".." in instance[0]: instance = (instance[0].replace("..", "."), instance[1])

	for part in [1, 2]:

		start = time.time()

		total_solutions = 0

		for instance in instances:

			cache = {}

			if part == 1:
				s, blocks = instance[0], instance[1]
			else:
				s = "?".join([instance[0] for i in range(5)]) # + "."
				blocks = instance[1] * 5		

			answers = (solve(s, blocks, [], 0, 0))
			total_solutions += answers

		elapsed = round((time.time() - start), 2)

		print(f"Resposta (parte {part}) -> {total_solutions} (tempo: {elapsed}s)")


