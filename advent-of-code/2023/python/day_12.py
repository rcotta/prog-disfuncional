import itertools as it
import time
import re

cache = None

def shape(s):

	ret = []
	count = 0

	for c in s:
		if c == '.':
			if count > 0:
				ret.append(count)
				count = 0
		if c == '#':
			count += 1

	if count > 0: ret.append(count)

	return ret


def solve(s, blocks, blocks_identified, block_reading, i):

	# block reading
	c = None if i == len(s) else s[i]
	ret = 0
	key = None

	if c == '?':
		ret += solve(s[:i] + '.' + s[i+1:], blocks, blocks_identified, block_reading, i)
		ret += solve(s[:i] + '#' + s[i+1:], blocks, blocks_identified, block_reading, i)

	else:

		if block_reading > 0:
			if c == '#':
				block_reading += 1
			elif c == '.' or c == None:
				blocks_identified = blocks_identified + [block_reading]
				block_reading = 0
			elif c == '?':
				pass # coberto na condição anterior!!!
		elif block_reading == 0 and c == '#':
			block_reading = 1

		# dp
		key = (tuple(blocks_identified), block_reading, i)
		if key in cache: return cache[key]
	
		# condição de parada
		if len(s) == i:
			computed_shape = shape(s)
			ret = 1 if blocks == computed_shape else 0
			cache[key] = ret
		
		else:

			# prunning ... melhorou performance em 200x+
			skip = False
			if c == '.':
				partial_shape = shape(s[:i])
				len_partial_shape = len(partial_shape)
				if len_partial_shape and partial_shape != blocks[:len_partial_shape]:
					skip = True

			if skip: ret = 0
			else: ret = solve(s, blocks, blocks_identified, block_reading, i + 1)
			cache[key] = ret
				
	return ret

with open("input/day_12.input", "r") as f:

	ans = 0
	infos = [line.strip().split(" ") for line in f.readlines()]
	instances = [(info[0], list(map(int, info[1].split(",")))) for info in infos]


	instance_num = 0

	for part in [1, 2]:

		for instance in instances:

			instance_num += 1
			cache = {}

			if part == 1:
				s, blocks = instance[0], instance[1]
			else:
				s = "?".join([instance[0] for i in range(5)]) + "."
				blocks = instance[1] * 5		

			start = time.time()
			answers = (solve(s, blocks, [], 0, 0))
			ans += answers
			end = time.time()

			# print(f"Processado {instance_num}/{len(instances)} = {answers} em {round((end-start), 2)}s")

		print(f"Resposta (parte {part}) -> {ans}")


