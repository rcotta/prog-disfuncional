import re
import copy
from time import time
from itertools import chain

X, Y, Z = 0, 1, 2


def intercept(s1, s2):
	"""
	Dados dois "retângulos", cada um definido pelas coordenadas
	[(x1, y1, z1), (x2, y2, z2)], verifica se os dois se
	sobrepõem nos eixos x e y (sem considerar z)
	"""
	for i in [X, Y]:
		s1_pmin, s1_pmax = min(s1[0][i], s1[1][i]), max(s1[0][i], s1[1][i])
		s2_pmin, s2_pmax = min(s2[0][i], s2[1][i]), max(s2[0][i], s2[1][i])
		if s1_pmin > s2_pmax or s1_pmax < s2_pmin: return False

	return True


def build_z_indexes(fs):
	"""
	Cria um dict onde a chave é o valor de z-max e o valor
	é uma lista de blocos com o z-max dado
	"""
	max_z = {}
	for k, v in fs.items():
		max_val = v[1][Z]
		if not max_val in max_z: max_z[max_val] = set()
		max_z[max_val].add(k)
	
	return max_z


def move_down(bricks, mi):
	"""
	Move todos os blocos para baixo, até que encontrem o chão (z==1)
	ou até que encontrem um outro bloco em seu estado final (apoiado
	no chão ou apoiado em outro bloco também em estado final)
	"""

	state = copy.deepcopy(bricks) # variável que representa os blocks depois de estarem todos estabilizados
	resolved = set([k for k, v in state.items() if v[0][Z] == 1]) # lista de indices de blocos que já encontram estado final

	z_max = build_z_indexes(state) # lista os blocos indexados pelos respectivos z-max

	moved = True # flag que indica se algum bloco foi movido na última execução do loop
	while moved:
		moved = False

		# como o movimento dos blocos dependem do z_max mais abaixo, devemos mover
		# os blocos do menor z_max para o maior z_max, considerando somente aqueles
		# que não estão em resolved
		bricks_to_move = [item for items in z_max.values() for item in items if item not in resolved]

		# para cada um dos blocos, verificar se ele pode ser movido ...
		for i_brick_to_move in bricks_to_move:
			
			# verificar se ele está apoiado em algum block que o impeça de descer

			# potenciais blocos que o apóiam tem 
			# z_max igual ao z_min do bloco atual - 1, logo
			# podemos considerar apenas esses no loop
			potential_bricks_z_max = state[i_brick_to_move][0][Z] - 1
			bottom_bricks = z_max[potential_bricks_z_max] if potential_bricks_z_max in z_max else []

			blocked = False
			for i_bottom_brick in bottom_bricks:

				i, j = min(i_brick_to_move, i_bottom_brick), max(i_brick_to_move, i_bottom_brick)
				if not mi[(i, j)]: continue

				# se i_bottom_brick está apoiado em um bloco que já encontrou seu estado final,
				# então i_bottom_brick também encontrou seu estado final (e pode ir para resolved)
				if i_bottom_brick in resolved:
					resolved.add(i_brick_to_move)
					

				blocked = True
				break

			if not blocked:

				moved = True # tivemos movimento
				prev_z_max = state[i_brick_to_move][1][Z]

				# move o bloco
				state[i_brick_to_move][0][Z] -= 1
				state[i_brick_to_move][1][Z] -= 1

				# atualiza o z_max
				z_max[prev_z_max].remove(i_brick_to_move)
				if not state[i_brick_to_move][1][Z] in z_max: z_max[state[i_brick_to_move][1][Z]] = set()
				z_max[state[i_brick_to_move][1][Z]].add(i_brick_to_move)

				# se chegou ao chão, está resolvido
				if state[i_brick_to_move][0][Z] == 1:
					resolved.add(i_brick_to_move)

	return state


def del_chain(id, fs, supported_by, supports):

	deleted = set([id])
	p = 0

	while p < len(deleted):
		
		cur = list(deleted)[p]
		p += 1

		# for k, v in fs.items(): << original
		# to_inspect = {k:v for k, v in fs.items() if v[0][Z] > fs[id][1][Z]}
		ids = set(chain.from_iterable([supports[k] for k in deleted]))
		to_inspect = {k:fs[k] for k in ids if k not in deleted}
		for k, v in to_inspect.items():

			# o próprio nó, não precisa verificar
			if cur == k: continue

			# o nó está no chão, ignorar
			if v[0][Z] == 1: continue

			# o nó k não vai sofrer consequências após a exclusão
			# de id, pois ele está no chão ou é suportado por outros
			# nós
			# if len([i for i in supported_by[k] if i not in deleted]) > 0: continue
			ignore = False
			for i in supported_by[k]:
				if i not in deleted:
					ignore = True
					break
			if ignore: continue

			deleted.add(k)
			

	return len(deleted) - 1


with open("input/day_22.input", "r") as f:

	start = time()

	bricks = {}

	lines = [line.strip() for line in f.readlines()]
	for i in range(len(lines)):
		nums = list(map(int, re.findall("[0-9]+", lines[i])))
		p1, p2 = nums[0:3], nums[3:]
		if (p2[Z] < p1[Z]):
			p1, p2 = p2, p1
		bricks[i] = (p1, p2)

	mi = {} # (i, j) -> True | False

	for i in range(len(bricks) - 1):
		for j in range(i + 1, len(bricks)):
			mi[(i, j)] = intercept(bricks[i], bricks[j])

	fs = move_down(bricks, mi)

	# 1. A não apóia outros blocks
	# 2. ou os blocks apoiados por A, também são apoiados por Z
	supports = {} # quem i está suportando?
	supported_by = {} # quem suporta i?
	for k1, v1 in fs.items():
		supports[k1] = set()
		for k2, v2 in fs.items():
			if (k1 == k2): continue
			i, j = min(k1, k2), max(k1,k2)
			if mi[(i, j)] and (v1[1][Z] == v2[0][Z] - 1):
				supports[k1].add(k2)
				if not k2 in supported_by: supported_by[k2] = set()
				supported_by[k2].add(k1)

	print(f"Fim preparação ... (em {round(time() - start)}s)")

	for part in [1, 2]:

		ans = 0
		start = time()

		if part == 2:
			for k in fs.keys():
				ans += del_chain(k, fs, supported_by, supports)

		if part == 1:

			eligible = set()
			for k, v in fs.items():
				
				if len(supports[k]) == 0:
					eligible.add(k)
					continue

				unique = False
				for idx_cmp in supports[k]:
					if len(supported_by[idx_cmp]) == 1:
						unique = True
						break

				if not unique: eligible.add(k)
			ans = len(eligible)

		print(f"Resposta (parte {part}) -> {ans} (em {round(time() - start)}s)")


	