with open("day_11.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]
	galaxies = set() # (x, y)
	incs = {} # (x, y): [inc_x, inc_y]
	
	h = len(lines)
	w = len(lines[0])

	# salvando coordenadas das galáxias em galaxies
	for y in range(h):
		for x in range(w):
			if lines[y][x] == '#':
				galaxies.add((x, y))

	# expansão vertical
	for y in range(h):
		n = sum([1 for galaxy in galaxies if galaxy[1] == y]) # n = # de galáxias na linha
		if n == 0: # se não tenho galáxias na linha y
			to_expand = [item for item in galaxies if item[1] > y] # galáxias com y > que linha expandida
			for galaxy in to_expand:
				if not galaxy in incs: incs[galaxy] = [0, 1]
				else: incs[galaxy][1] += 1

	# expansão horizontal
	for x in range(w):
		n = sum([1 for galaxy in galaxies if galaxy[0] == x])
		if n == 0: # se não tenho galáxias na coluna x
			to_expand = [item for item in galaxies if item[0] > x] # galáxias com y > que linha expandida
			for galaxy in to_expand:
				if not galaxy in incs: incs[galaxy] = [1, 0]
				else: incs[galaxy][0] += 1

	tmp = set()

	for galaxy in galaxies:
		if galaxy in incs:
			galaxy = (galaxy[0] + incs[galaxy][0], galaxy[1] + incs[galaxy][1])
		tmp.add(galaxy)

	# galáxias expandidas
	galaxies = tmp

	galaxies_list = list(galaxies)
	dist = 0

	for i in range(len(galaxies_list) - 1):
		for j in range(i + 1, len(galaxies_list)):
			a, b = galaxies_list[i], galaxies_list[j]
			dist += abs(a[0] - b[0]) + abs(a[1] - b[1])

	print(f"Resposta -> {dist}")


		
	

