
with open("input/day_3.input") as f:

	line = f.readline().strip()

	houses = set()

	coords = [(0, 0), (0, 0)]
	houses.add((0,0))
	moves = {"<": [-1, 0], ">": [1, 0], "^": [0, -1], "v": [0, 1]}

	who = 0
	for c in line:
		who = (who + 1) % 2
		move = moves[c]
		coords[who] = (coords[who][0] + move[0], coords[who][1] + move[1])
		houses.add(coords[who])

	ans = len(houses)
	print(f"Resposta -> {ans}")


