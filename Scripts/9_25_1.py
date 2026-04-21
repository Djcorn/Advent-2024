import math
import pathlib
import numpy

f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_9_25.txt"), 'r')
sum = 0
fresh_array = []
while True:
    line = f.readline()
    line = line[:-1]
    if not line:
        break
    line =line.split(',')

    fresh_array.append([float(item) for item in line])

longest = 0
shortest_1 = 0
shortest_2 = 0
for i in range(0,len(fresh_array)):
    for j in range(i+1,len(fresh_array)):
        area = ((abs(fresh_array[i][0]-fresh_array[j][0]))+1)*((abs(fresh_array[i][1]-fresh_array[j][1]))+1)

        if area > longest :
            longest = area
            shortest_1 = i
            shortest_2 = j
print(fresh_array[shortest_1])
print(fresh_array[shortest_2])
print(longest)


