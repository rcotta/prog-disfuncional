import re

SIZE = 1000

def exec_part_1(grid, p1, p2, action):
	
	for y in range(p1[1], p2[1] + 1):
		for x in range(p1[0], p2[0] + 1):
			if action == "turn on": grid[y][x] = 1
			elif action == "turn off": grid[y][x] = 0
			elif action == "toggle": grid[y][x] = 0 if grid[y][x] == 1 else 1


def exec_part_2(grid, p1, p2, action):
	
	for y in range(p1[1], p2[1] + 1):
		for x in range(p1[0], p2[0] + 1):
			if action == "turn on": grid[y][x] += 1
			elif action == "turn off":
				if grid[y][x] > 0: grid[y][x] -= 1
			elif action == "toggle": grid[y][x] += 2


with open("input/day_6.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]

	for part in [1, 2]:

		grid = [[0 for i in range(SIZE)] for j in range(SIZE)]
		ans = 0

		for line in lines:

			c = list(map(int, re.findall("[0-9]+", line)))
			action = "toggle"
			if "turn off" in line: action = "turn off"
			elif "turn on" in line: action = "turn on"

			p1 = (min(c[0], c[2]), min(c[1], c[3]))
			p2 = (max(c[0], c[2]), max(c[1], c[3]))

			if part == 1:
				exec_part_1(grid, p1, p2, action)
			else:
				exec_part_2(grid, p1, p2, action)

		ans = sum([sum(row) for row in grid])
		print(f"Resposta (parte {part}) --> {ans}")









		