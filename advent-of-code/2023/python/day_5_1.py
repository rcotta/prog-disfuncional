

def corresp(source_type, origin_type, source):
	
	k = (source_type, origin_type)

	for item in conv[k]:

		if source >= item[1] and source <= item[1] + item[2]:
			return item[0] + (source - item[1])

	return source

def seed_to_location(seed):

	soil = corresp('seed', 'soil', seed)
	fer = corresp('soil', 'fertilizer', soil)
	water = corresp('fertilizer', 'water', fer)
	light = corresp('water', 'light', water)
	temperature = corresp('light', 'temperature', light)
	humidity = corresp('temperature', 'humidity', temperature)
	location = corresp('humidity', 'location', humidity)
	
	return location


with open("input/day_5.input", "r") as f:

	seeds = None
	conv = {} # [(origem, destino)] = []
	current_key = None

	lines = [line.strip() for line in f.readlines()]

	for line in lines:
		if line == "": continue

		if line.startswith("seeds:"):
			seeds = [int(s) for s in line.split(": ")[1].split(" ")]

		elif line.endswith("map:"):
			parts = line.split(" ")[0].split("-to-")
			current_key = (parts[0], parts[1])

		else:
			nums = [int(s) for s in line.split(" ")]

			if not current_key in conv:
				conv[current_key] = []

			conv[current_key].append(nums)

	locations = [seed_to_location(seed) for seed in seeds]

	print(f"Resposta -> {min(locations)}")



