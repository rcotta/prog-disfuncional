import math
from operator import add
from collections import deque

# constantes com incrementos nas 4 direções
x_l, x_r, y_u, y_d = (-1, 0), (1, 0), (0, -1), (0, 1)
tile_types = ["F", "7", "J", "L", "|", "-"]

# x left/right, y up/down ... sempre na ordem x_l, x_r, y_u, y_d
tile_increments = [[x_r, y_d], [x_l, y_d], [x_l, y_u], [x_r, y_u], [y_u, y_d], [x_l, x_r]]

# os destinos (no formato de incremento) para cada um dos tipos de tiles
tile_types_increments = {i[0]:i[1] for i in zip(tile_types, tile_increments)}

# imprime o mapa, dado em formato de tiles,
# monstrando apenas os tiles que fazem parte do encanamento
def print_map(tiles):

	for y in range(len(tiles)):
		out = []
		for x in range(len(tiles[y])):
			coord = (x, y)
			out.append(tiles[y][x] if coord in visited else ' ')
		print(" ".join(out))


# soma de tuples
def t_add(a: tuple, b:tuple) -> tuple:
	return tuple(map(add, a, b))


# dado um tile de configuração desconhecida, retorna o tile válido
# utilizado para descobrir o tipo de tile sobrescrito por S
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

	# se o tamanho do loop é dist, o ponto mais longe da origem
	# está a dist/2 de distância
	print(f"Reposta: {math.ceil(dist/2)}")

	# print_map(tiles)


	pass
