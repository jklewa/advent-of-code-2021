import requests
import itertools
import io

# sample = io.StringIO('''forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2''')
# commands = sample
commands = open('data/2.input', 'r')

moves = {
	'forward': (1, 0, 0),
	'down': (0, 1, 1),
	'up': (0, -1, -1),
}

position = [0, 0]
for c in commands:
	direction, steps = c.strip().split(' ')
	move = moves[direction]
	position[0] = position[0] + move[0] * int(steps)
	position[1] = position[1] + move[1] * int(steps)

print(f'Position: {position} Answer: {position[0] * position[1]}')

# sample = io.StringIO('''forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2''')
# commands = sample
commands = open('data/2.input', 'r')

position = [0, 0, 0]
for c in commands:
	direction, steps = c.strip().split(' ')
	move = moves[direction]
	position[0] = position[0] + move[0] * int(steps)
	position[1] = position[1] + position[2] * move[0] * int(steps)
	position[2] = position[2] + move[2] * int(steps)

print(f'Position: {position} Answer: {position[0] * position[1]}')