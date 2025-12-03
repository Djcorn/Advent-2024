import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_3_25.txt"), 'r')
sum = 0
while True:
    line = f.readline()
    line = line[:-1]
    line_array = [int(char) for char  in line]
    if not line:
        break
    first = 1
    first_index = 0
    for i in range(0,len(line_array)-1):
        if line_array[i] > first:
            first = line_array[i]
            first_index = i
    print(first)
    second = 1
    second_index = 1
    for i in range(first_index+1,len(line_array)):
        if line_array[i] > second :
            second = line_array[i]
            first_index = i
    print(second)
    val = int(str(first)+str(second))
    sum += val
print(sum)

