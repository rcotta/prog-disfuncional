
with open("input/day_3.input") as f:

	line = f.readline().strip()

	houses = set()

	coords = (0, 0)
	houses.add(coords)
	moves = {"<": [-1, 0], ">": [1, 0], "^": [0, -1], "v": [0, 1]}

	for c in line:
		move = moves[c]
		coords = (coords[0] + move[0], coords[1] + move[1])
		houses.add(coords)

	ans = len(houses)
	print(f"Resposta -> {ans}")


