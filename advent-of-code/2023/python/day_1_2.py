

nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def find_number_name(s):

	for k, v in nums.items():
		if s.startswith(k): return v
	
	return None

def find_number(s):

	ret = [None, None]

	for i in range(len(s)):

		if s[i] in "0123456789":
			ret[0] = int(s[i])
			break

		num = find_number_name(s[i:])
		if num:
			ret[0] = num
			break

	for i in range(len(s)):

		if s[(len(s) - 1) - i] in "0123456789":
			ret[1] = int(s[(len(s) - 1) - i])
			break

		num = find_number_name(s[(len(s) - 1) - i:])
		if num:
			ret[1] = num
			break

	return ret[0] * 10 + ret[1]


with open("input/day_1.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]
	answer = sum([find_number(line) for line in lines])

	print(f"Resposta -> {answer}")


