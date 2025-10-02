import pathlib
import numpy
import copy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_9_24_test.txt"), 'r')
line = f.readline()
list = []
n = 0
numbers = 0
for i, char in enumerate(line):
    if i%2==1:
        for j in range(0, int(char)):
            list.append(".")
            i = i-1
    else:
        for j in range(0,int(char)):
            list.append(n)
            numbers+=1
        n+=1
print(list)
for i in range(0,numbers):
    if list[-i-1] == ".":
        continue
    list[list.index(".")] = list[-i-1]
    list[-i-1] = "."
    if list.index(".") == numbers:
        break
total = 0
for i,_ in enumerate(list):
    if list[i] == ".":
        break
    total += i * int(list[i])
print(total)
print(list)