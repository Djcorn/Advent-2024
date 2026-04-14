import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_5_25_test.txt"), 'r')
sum = 0
fresh_array = []
while True:
    line = f.readline()
    line = line[:-1]
    if not line:
        break
    line = line.split('-')
    line[0]= int(line[0])
    line[1]= int(line[1])
    found = 0
    diff = (line[1] - line[0])+1
    for i in range(0,len(fresh_array)-1,2):
        if line[0]>fresh_array[i] and line[1] < fresh_array[i+1]:
            diff = 0
            break
        if line[0] < fresh_array[i + 1] and line[1] > fresh_array[i + 1]:
            diff -= (fresh_array[i + 1]+1) - line[0]

        if line[1] > fresh_array[i] and line[0] < fresh_array[i]:
            diff -= (line[1]+1) - (fresh_array[i])

    sum += diff
    print(sum)

    fresh_array.append(line[0])
    fresh_array.append(line[1])

    print(fresh_array)
