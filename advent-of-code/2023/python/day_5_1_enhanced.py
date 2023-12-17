# Versão revisada da solução do dia 5 / parte 1, após solução da parte 2.

table = []

def transpose(items, table_row):

	ret = []

	for item in items:

		t = [record for record in table_row if item in range(record['src'][0], record['src'][1] + 1)]
		if len(t):
			inc = t[0]['dest'] - t[0]['src'][0]
			item += inc

		ret.append(item)

	return ret


with open("input/day_5.input", "r") as f:

	lines = [line.strip() for line in f.readlines() if line.strip() != ""]

	items = list(map(int, lines[0].split(" ")[1:]))

	for i in range(1, len(lines)):
		line = lines[i]
		if "map:" in line:
			table.append([])
		else:
			dest, x1, length = list(map(int, line.split(" ")))
			table[len(table) - 1].append({'src': (x1, x1 + length - 1), 'dest': dest})

	for i in range(len(table)):
		items = transpose(items, table[i])

	print(f"Resposta -> {min(items)}")
