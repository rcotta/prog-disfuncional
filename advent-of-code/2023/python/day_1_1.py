 
def find_number(s):

	ret = [None, None]

	for i in range(len(s)):

		if not ret[0] and s[i] in "0123456789":
			ret[0] = int(s[i])

		if not ret[1] and s[(len(s) - 1) - i] in "0123456789":
			ret[1] = int(s[(len(s) - 1) - i])

		if not None in ret: break

	return ret[0] * 10 + ret[1]


with open("input/day_1.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]
	answer = sum([find_number(line) for line in lines])

	print(f"Resposta -> {answer}")


