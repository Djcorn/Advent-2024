import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_2_25.txt"), 'r')
sum = 0

line = f.readline()
list = line.split(",")
for item in list:
    bounds = item.split("-")
    for i in range(int(bounds[0]),int(bounds[1])+1):
        string_i = str(i)
        midpoint = len(string_i) // 2
        first_half = string_i[:midpoint]
        second_half = string_i[midpoint:]
        if first_half == second_half:
            sum += i

print(sum)
