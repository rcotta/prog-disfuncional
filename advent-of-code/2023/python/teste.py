from time import time


def coins_dp(v):

	global coin_types
	# global iter

	mem = {coin_type:(1, [coin_type]) for coin_type in coin_types}

	ret = (float('inf'), [])

	for i in range(v):

		if i in mem:
			tmp = mem[i]
			for coin_type in coin_types:
				# iter += 1
				target = (tmp[0] + 1, tmp[1] + [coin_type])
				if (i + coin_type) in mem: mem[i + coin_type] = min(mem[i + coin_type], target)
				else: mem[i + coin_type] = target

		if v in mem:
			ret = mem[v]
			break

	return ret


LIMIT = 10
def coins_mem(v):

	global iter
	global mem

	# iter += 1
	if v in mem: return mem[v]

	t = 1
	while not t * LIMIT in mem and t * LIMIT < v:
		coins_mem(t * LIMIT)
		t += 1

	ret = (float('inf'), [])

	if v in coin_types:
		ret = (1, [v])

	else:

		for coin_type in coin_types:

			next_value = v - coin_type

			tmp = mem[next_value] if next_value in mem else coins_mem(next_value)
			tmp = (tmp[0] + 1, tmp[1] + [coin_type])
				
			ret = min(ret, tmp)

	mem[v] = ret
	return ret
			
iter = 0
coin_types = [2, 8, 12, 13, 17, 18]

for change in [100000]:

	start = time()
	iter = 0
	mem = {coin_type:(1, [coin_type]) for coin_type in coin_types}
	print(f"1. Change for {change} in {coins_mem(change)[0]} coins with {iter} iterations in {round((time() - start), 2)}s.")

	# iter = 0
	# print(f"2. Change for {change} in {coins_dp(change)[0]} coins with {iter} iterations in {round((time() - start), 2)}s.")
