

def solve_p1(s):
	"""
	Retorna duas tuplas, representando os dígitos à esquerda e a direita,
	no formato (<posição>, <dígito>)
	"""

	l = (float('inf'), 0)
	r = (float('-inf'), 0)

	for digit in [str(i) for i in range(1, 10)]:
		pos = s.find(digit) # busca dígito à esquerda
		if pos >=0: l = min((pos, int(digit)), l)

		pos = s.rfind(digit) # busca dígito à direita
		if pos >=0: r = max((pos, int(digit)), r)

	return l, r


def solve_p2(s):

	# toma a solução de p1 como ponto de partida
	l, r = solve_p1(s)

	num_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

	for num_name in num_names:
		pos = s.find(num_name) # busca string com nome do dígito à esquerda
		if pos >=0: l = min((pos, num_names.index(num_name) + 1), l) # mantem o achado com MENOR posição

		pos = s.rfind(num_name) # busca string com nome do dígito à direita
		if pos >=0: r = max((pos, num_names.index(num_name) + 1), r) # mantem o achado com MAIOR posição

	return l, r	


with open("input/day_1.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]

	for part in [1, 2]:

		ans = 0

		for line in lines:
			
			l, r = solve_p1(line) if part == 1 else solve_p2(line)
			num = l[1] * 10 + r[1]
			ans += num

		print(f"Resposta (parte {part}) -> {ans}")