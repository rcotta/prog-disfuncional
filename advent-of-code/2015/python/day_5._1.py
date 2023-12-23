

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

def is_nice(s):

	# regra 1
	if sum([s.count(v) for v in "aeiou"]) < 3: return 0

	# regra 2
	found = False
	for i in range(ord("a"), ord("z") + 1):
		search = chr(i) + chr(i)
		if search in s:
			found = True
			break
	if not found: return 0

	# regra 3
	found = (sum([1 if search in s else 0 for search in ["ab", "cd", "pq", "xy"]]) > 0)
	if found: return 0

	return 1

def is_nice_part_2(s):

	# regra 2 -> aXa
	found = False
	for i in range(len(s) - 2):
		if s[i] == s[i + 2]:
			found = True
			break
	
	if not found: return 0

	# regra 1
	pairs = {}
	for i in range(len(s) - 1):
		pair = s[i] + s[i+1]
		if not pair in pairs: pairs[pair] = []
		pairs[pair].append(i)
		if len(pairs[pair]) > 1:
			if pairs[pair][-1] - pairs[pair][0] > 1:
				return 1

	return 0






with open("input/day_5.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]

	# parte 1
	ans = 0
	for line in lines:
		ans += is_nice(line)

	print(f"Resposta (parte 1) --> {ans}")

	# parte 2
	ans = 0
	for line in lines:
		ans += is_nice_part_2(line)

	print(f"Resposta (parte 2) --> {ans}")
