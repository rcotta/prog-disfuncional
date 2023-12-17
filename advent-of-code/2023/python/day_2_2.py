import re

def validate_game(info):

	# only 12 red cubes, 13 green cubes, and 14 blue cubes
	cubes = {'red': 0, 'green': 0, 'blue': 0}

	nums = [int(token) for token in re.findall("[0-9]+", info)]
	colors = re.findall("Game|red|blue|green", info)

	for i in range(1, len(nums)):
		cubes[colors[i]] = max(nums[i], cubes[colors[i]])

	return cubes['red'] * cubes['green'] * cubes['blue']



with open("input/day_2.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]
	answer = sum([validate_game(line) for line in lines])

	print(f"Resposta -> {answer}")
