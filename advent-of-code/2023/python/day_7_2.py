
cards = "AKQT98765432J" # J passa a ser a carta mais fraca

def compute_strength(hand):
	
	ret = []

	# conta repetições, maior contagem na frente
	cards_counts = {c:hand.count(c) for c in hand}

	# trata J como coringa
	if "J" in cards_counts and cards_counts["J"] != 5:
		# encontra o item de maior contagem
		max_item = sorted({k:v for k,v in cards_counts.items() if k != "J"}.items(), key=lambda entry: -entry[1])[0]
		cards_counts[max_item[0]] += cards_counts["J"]
		cards_counts["J"] = 0	

	# ordena do maior para o menor, traz somente 2 primeiras posições
	# (ou completa com uma posição adicional se tivermos um five)
	lcounts = sorted(cards_counts.values(), reverse=True)
	if len(lcounts) == 1: counts = (5,0)
	else: counts = (lcounts[0], lcounts[1])

	ret.append(counts)

	for c in hand:
		ret.append(len(cards) - cards.index(c)) # determina um valor, sendo A o maior valor

	return ret



with open("input/day_7.input", "r") as f:

	# 1. determinar as contagens de cartas e salvar em tupla de tamanho 2,
	# ordenada da maior para a menor (ex: (5,0) - five, (2,2) - 2 pares, (1,1) - sem jogo)
	#
	# 2. colocar a tupla e os índices das cartas individualmente em um array
	#
	# 3. utilizar o sorted para ordenar (ele é capaz de comparar tuplas)

	data = []

	while line := f.readline().strip():
		hand, bet = line.split(" ")
		strength = compute_strength(hand)
		hand_data = strength +[hand] + [int(bet)]
		data.append(hand_data)

	ans = 0
	data = sorted(data)
	for i in range(len(data)):
		ans += (i + 1) * data[i][-1]

	print(f"Resposta -> {ans}")
