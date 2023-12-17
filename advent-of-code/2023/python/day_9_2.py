import re

def compute_diff(arr):
	return [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]


with open("input/day_9.input", "r") as f:

	ans = 0
	while line := f.readline().strip():

		seq = list(map(int, re.findall("-?[0-9]+", line)))

		heads = []
		while (len(seq) != seq.count(0)):
			heads.append(seq[0]) # salva último número
			seq = compute_diff(seq)
		
		tmp = heads.pop()
		while (len(heads)): tmp = heads.pop() - tmp
		ans += tmp

	print(f"Resposta -> {ans}")