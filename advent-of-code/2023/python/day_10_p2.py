import math
from operator import add
from collections import deque

# soma tuples, retorna tuple
def t_add(a: tuple, b:tuple) -> tuple:
	return tuple(map(add, a, b))


# constantes com incrementos nas 4 direções
x_l, x_r, y_u, y_d = (-1, 0), (1, 0), (0, -1), (0, 1)
tile_types = ["F", "7", "J", "L", "|", "-"]

# x left/right, y up/down ... sempre na ordem x_l, x_r, y_u, y_d
tile_increments = [[x_r, y_d], [x_l, y_d], [x_l, y_u], [x_r, y_u], [y_u, y_d], [x_l, x_r]]

# preciso?
tile_types_increments = {i[0]:i[1] for i in zip(tile_types, tile_increments)}

directions = {'W': x_l, 'E': x_r, 'N': y_u, 'S': y_d, 'NW': t_add(x_l, y_u), 'NE': t_add(x_r, y_u), 'SW': t_add(x_l, y_d), 'SE': t_add(x_r, y_d)}

def print_zoomed_map(zoomed):

	for line in zoomed: print("".join(line))


# conta grids de 3x3 compostos inteiramente por pontos
def count_empties(data):

	x, y = 0, 0
	w, h = len(data[0]), len(data)
	result = 0

	for y in range(0, h, 3):
		for x in range(0, w, 3):
			if data[y][x:x+3] == ['.', '.', '.'] and data[y+1][x:x+3] == ['.', '.', '.'] and data[y+2][x:x+3] == ['.', '.', '.']:
				result += 1

	return result


def flood_fill(data, p):

	search_char = '.'
	replace_char = 'x'
	w = len(data[0])
	h = len(data)
	q = {p}

	while (len(q)):
		
		p = q.pop()

		data[p[1]][p[0]] = replace_char

		nps = [t_add(p, inc) for inc in directions.values()]

		for np in nps:
			if np[0] < 0 or np[0] >= w or np[1] < 0 or np[1] >= h: continue # fora dos limites da imagem
			if data[np[1]][np[0]] != search_char: continue
			if np in q: continue
			q.add(np)

	return data
		
		


def zoom_tiles(tiles):

	w = len(tiles[0])
	h = len(tiles)

	t = {
		'-': ['...', '***', '...'],
		'|': ['.*.', '.*.', '.*.'],
		'F': ['...', '.**', '.*.'],
		'7': ['...', '**.', '.*.'],
		'J': ['.*.', '**.', '...'],
		'L': ['.*.', '.**', '...'],
		'.': ['...', '...', '...']
	}

	ret = [['.' for j in range(w * 3)] for i in range(h * 3)]

	for y in range(h):
		for x in range(w):
			out = t[tiles[y][x]]
			for i in range(3):
				ret[y * 3 + i][x * 3:x*3 + 4] = out[i]

	return ret


def print_map(tiles):

	for y in range(len(tiles)):
		out = []
		for x in range(len(tiles[y])):
			coord = (x, y)
			# out.append(tiles[y][x] if coord in visited else ' ')
			out.append(tiles[y][x])
		print(" ".join(out))



def get_valid_pipe_type(current_tile_coords):

	# top, left, bottom, right
	valids = []
	for inc in [x_l, x_r, y_u, y_d]:
		
		dest_coord = t_add(current_tile_coords, inc) # coord do tile que vamos inspecionar

		# verifica se coordenada a ser analisada está nos limites
		if dest_coord[0] < 0 or dest_coord[0] >= len(tiles[0]): continue
		if dest_coord[1] < 0 or dest_coord[1] >= len(tiles): continue

		dest_type = tiles[dest_coord[1]][dest_coord[0]]
		if dest_type == '.': continue

		dest_increments = tile_types_increments[dest_type] # incrementos do tile que estamos inspecionando

		# se algum desses incrementos nos levam de volta para a coordenada original, o tile é válido
		# salvar o inc correspondente pois nos ajuda a buscar o tipo do tile
		if current_tile_coords in [t_add(dest_coord, inc) for inc in dest_increments]:
			valids.append(inc)

	valid_increments_index = tile_increments.index(valids)
	return tile_types[valid_increments_index]


# calcula as possíveis coordenadas para o próximo movimento, retorna
# somente coordenadas de tiles não visitados (no cenário comum, retorna array de 1 item)
def get_next_tile_coords(coords):

	tile_type = tiles[coords[1]][coords[0]]
	potential = [t_add(coords, inc) for inc in tile_types_increments[tile_type]]
	result = [ret for ret in potential if ret not in visited]

	return result


with open("day_10.input", "r") as f:

	visited = {} # {(x,y) : dist}

	tiles = [[c for c in line.strip()] for line in f.readlines()]

	current_tile_coords = None

	# busca tile inicial, inicializa vars e realiza ajustes ...
	for y in range(len(tiles)):
		if "S" in tiles[y]: # encontrou ...

			current_tile_coords = (tiles[y].index("S"), y) # salva a localização ...
			visited[current_tile_coords] = 0 # marca como visitado, com distância zero
			tiles[y][tiles[y].index("S")] = get_valid_pipe_type(current_tile_coords) # descobre tipo do tile, e atualiza
			break

	dist = 0
	while True:

		# nos casos regulares, como cada cano tem uma entrada
		# e uma saída, a chamada irá retornar 1 único item
		# até voltar à origem
		potential_tiles = get_next_tile_coords(current_tile_coords)
		if potential_tiles: current_tile_coords = potential_tiles[0]
		else: break

		dist += 1
		visited[current_tile_coords] = dist

	width = len(tiles[0])
	height = len(tiles)

	# limpa tiles que não pertencem ao mapa
	for y in range(height):
		for x in range(width):
			if not (x, y) in visited: tiles[y][x] = '.'

	# adiciona moldura
	tiles.insert(0, ['.' for i in range(width)])
	tiles.append(['.' for i in range(width)])
	for row in tiles:
		row.insert(0, '.')
		row.append('.')

	# print_map(tiles)
	# print("\n\n")

	zoomed = zoom_tiles(tiles)

	# print_zoomed_map(zoomed)
	# print("\n\n")

	zoomed = flood_fill(zoomed, (0, 0))

	# print_zoomed_map(zoomed)
	# print("\n\n")

	total = count_empties(zoomed)
			
	print(f"Resposta --> {total}")
		



	pass
