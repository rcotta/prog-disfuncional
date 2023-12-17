import re

def validate_game(info):

	# only 12 red cubes, 13 green cubes, and 14 blue cubes
	max_cubes = {'red': 12, 'green': 13, 'blue': 14}

	nums = [int(token) for token in re.findall("[0-9]+", info)]
	colors = re.findall("Game|red|blue|green", info)

	valid = True
	for i in range(1, len(nums)):
		if nums[i] > max_cubes[colors[i]]:
			valid = False
			break

	return (nums[0], valid)



with open("input/day_2.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]
	answer = sum([game[0] for game in [validate_game(line) for line in lines] if game[1]])

	print(f"Resposta -> {answer}")
