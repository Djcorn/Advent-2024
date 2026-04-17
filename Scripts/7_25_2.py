import pathlib
import numpy as np

f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_7_25.txt"), 'r')
sum = 0
fresh_array = []
while True:
    line = f.readline()
    line = line[:-1]
    if not line:
        break
    fresh_array.append(list(line))

for i in range(0,len(fresh_array)-1):
    for j in range(0,len(fresh_array[i])-1):
        if fresh_array[i][j] == 'S':
            fresh_array[i+1][j] = '|'
        if fresh_array[i][j] == '^' and fresh_array[i-1][j] == '|':
            if fresh_array[i+1][j-1] != '^':
                fresh_array[i+1][j - 1] = '|'

        if fresh_array[i][j] == '|' and fresh_array[i+1][j] != '^':
            fresh_array[i+1][j] = '|'

print(fresh_array)
print(sum)