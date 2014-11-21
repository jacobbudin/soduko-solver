#!/usr/bin/env python3

def get_possibilities(soduko, block, row, col):
	if soduko[block][row][col]:
		return [soduko[block][row][col]]

	possibilities = set([1,2,3,4,5,6,7,8,9])

	# Check block
	for x in range(0, 3):
		for y in range(0, 3):
			possibilities.discard(soduko[block][x][y])

	# Check column
	for i in range(block % 3, 9, 3):
		for j in range(0, 3):
			possibilities.discard(soduko[i][j][col])

	# Check row
	for i in range(int(block/3)*3, (int(block/3)*3)+3):
		for j in range(0, 3):
			possibilities.discard(soduko[i][row][j])

	return possibilities

def solve_sudoku(soduko):
	position_possibilities = {}

	for block in range(0, 9):
		for row in range(0, 3):
			for col in range(0, 3):
				if soduko[block][row][col]:
					continue

				position_possibilities[(block, row, col)] = get_possibilities(soduko, block, row, col)

	for block, row, col in position_possibilities:
		possibilities = position_possibilities[(block, row, col)]

		if len(possibilities) == 1:
			soduko[block][row][col] = possibilities.pop()
			solve_sudoku(soduko)

	return soduko



samples = [
	[
		[
			[2, None, 1],
			[7, 3, 5],
			[9, 4, None]
		],
		[
			[None, None, 5],
			[2, None, None],
			[3, None, None]
		],
		[
			[None, None, 4],
			[None, 9, None],
			[None, None, None]
		],
		[
			[None, None, None],
			[None, 9, None],
			[5, 2, None]
		],
		[
			[None, 3, 2],
			[None, None, None],
			[9, 8, None]
		],
		[
			[None, 7, 9],
			[None, 6, None],
			[None, None, None]
		],
		[
			[None, None, None],
			[None, 1, None],
			[6, None, None]
		],
		[
			[None, None, 1],
			[None, None, 3],
			[8, None, None]
		],
		[
			[None, 3, 2],
			[9, 5, 6],
			[4, None, 7]
		],
	],
	[
		[
			[None, None, None],
			[8, None, 1],
			[5, 7, None]
		],
		[
			[None, 7, 3],
			[None, 2, None],
			[6, None, None]
		],
		[
			[None, None, None],
			[None, None, None],
			[None, 2, None]
		],
		[
			[None, None, None],
			[None, None, 3],
			[1, None, 7]
		],
		[
			[9, None, None],
			[None, 6, None],
			[None, None, 5]
		],
		[
			[6, None, 7],
			[8, None, None],
			[None, None, None]
		],
		[
			[None, 2, None],
			[None, None, None],
			[None, None, None]
		],
		[
			[None, None, 6],
			[None, 3, None],
			[7, 5, None]
		],
		[
			[None, 4, 5],
			[2, None, 9],
			[None, None, None]
		],
	]
]

for sample in samples:
	print(solve_sudoku(sample))
