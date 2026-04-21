import math
import pathlib
import numpy as np

f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_9_25_test.txt"), 'r')
def is_green(a,b):
    if a[0] < b[0] and a[1] < b[1]:
        for i in range(a[0],b[0]+1):
            for j in range(a[1],b[1]+1):
                if new_array.__contains__([i, j]):
                    continue
                else:
                    return False
    if a[0] > b[0] and a[1] > b[1]:
        for i in range(b[0],a[0]+1):
            for j in range(b[1],a[1]+1):
                if new_array.__contains__([i, j]):
                    continue
                else:
                    return False
    if a[0] < b[0] and a[1] > b[1]:
        for i in range(a[0],b[0]+1):
            for j in range(a[1],b[1]+1):
                if new_array.__contains__([i, j]):
                    continue
                else:
                    return False
    if a[0] > b[0] and a[1] < b[1]:
        for i in range(b[0],a[0]+1):
            for j in range(a[1],b[1]+1):
                if new_array.__contains__([i, j]):
                    continue
                else:
                    return False
    return True

fresh_array = []
while True:
    line = f.readline()
    line = line[:-1]
    if not line:
        break
    line =line.split(',')

    fresh_array.append([int(item) for item in line])




fresh_array.sort(key=lambda x: x[0])
fresh_array.sort(key=lambda x: x[1])

new_array = []
for i in range(0,len(fresh_array)):
    for j in range(i+1,len(fresh_array)):
        if (fresh_array[i][0] == fresh_array[j][0]):
            for x in range(fresh_array[i][1],fresh_array[j][1]+1):
                new_array.append([fresh_array[i][0],x])
        if (fresh_array[i][1] == fresh_array[j][1]):
            for x in range(fresh_array[i][0],fresh_array[j][0]+1):
                new_array.append([x,fresh_array[i][1]])



longest = 0
shortest_1 = 0
shortest_2 = 0
for i in range(0,len(fresh_array)):
    for j in range(i+1,len(fresh_array)):
        area = ((abs(fresh_array[i][0]-fresh_array[j][0]))+1)*((abs(fresh_array[i][1]-fresh_array[j][1]))+1)
        if area > longest:
            if is_green(fresh_array[i],fresh_array[j]):
                longest = area
                shortest_1 = i
                shortest_2 = j

print(fresh_array[shortest_1])
print(fresh_array[shortest_2])
print(longest)



