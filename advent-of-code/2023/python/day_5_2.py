
segments = [] # [(x1, x2)]
table = [] # [{src: (x1, x2), dest: <int>}]

def transpose(segments, table_row):

	ret = []

	for segment in segments:

		t = [item for item in table_row if segment[0] >= item['src'][0] and segment[1] <= item['src'][1]]
		if len(t):
			inc = t[0]['dest'] - t[0]['src'][0]
			segment = (segment[0] + inc, segment[1] + inc)

		ret.append(segment)

	return ret

def split_segments(segments, points):

	ret = sorted(segments)
	points = sorted(points)
	point_idx = 0
	i = 0

	while i < len(ret):
		
		segment = ret[i]

		while point_idx < len(points) and points[point_idx] < segment[0]:
			point_idx += 1

		if point_idx >= len(points): break

		point = points[point_idx]

		if point > segment[0] and point <= segment[1]:
			new_segment = (point, segment[1])
			ret[i] = (segment[0], point - 1)
			ret.insert(i + 1, new_segment)
			point_idx += 1
		
		i += 1
	
	return ret

with open("input/day_5.input", "r") as f:

	lines = [line.strip() for line in f.readlines() if line.strip() != ""]

	nums = list(map(int, lines[0].split(" ")[1:]))
	for i in range(0, len(nums), 2): segments.append((nums[i], nums[i] + nums[i+1] - 1))

	for i in range(1, len(lines)):
		line = lines[i]
		if "map:" in line:
			table.append([])
		else:
			dest, x1, length = list(map(int, line.split(" ")))
			table[len(table) - 1].append({'src': (x1, x1 + length - 1), 'dest': dest})


	for i in range(len(table)):
		points = sorted([item['src'][0] for item in table[i]] + [item['src'][1] for item in table[i]])
		segments = split_segments(segments, points)
		segments = transpose(segments, table[i])

	# print(f"Segmentos localidade: {segments}")
	ans = min([segment[0] for segment in segments])
	print(f"Resposta -> {ans}")

pass