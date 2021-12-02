""" Advent of Code 2021
    Day 1
"""

import itertools

data = open('data/1.input', 'r')

increase = 0
prev = None

for num in data:
    n = int(num)
    if prev is None or prev >= n:
        prev = n
    else:
        increase += 1
        prev = n

print(f'Increases: {increase}')

data = open('data/1.input', 'r')

increase = 0
prev = None
window_length = 3
window = [None] * window_length
for num in itertools.islice(data, window_length-1):
    window = window[1:window_length] + [int(num)]

for num in data:
    window = window[1:window_length] + [int(num)]
    n = sum(window)

    if prev is None or prev >= n:
        prev = n
    else:
        increase += 1
        prev = n

print(f'Window of {window_length} increases: {increase}')
