import pathlib
import numpy
import copy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_9_24.txt"), 'r')
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
n = n-1
print(list)
while n > 0:
    indices= [i for i, x in enumerate(list) if x == n]
    space = 1
    dot_indices = [i for i, x in enumerate(list) if x == "."]
    skips = 0
    for i in range(0,len(dot_indices)-1):
        if dot_indices[i] >= indices[0]:
            break
        if len(indices) == space:
            for j in range(0,space):
                list[dot_indices[j+skips]] = n
                list[indices[j]] = "."
            break
        elif dot_indices[i]+1 == dot_indices[i+1]:
            space+=1
        else:
            skips += space
            space=1


    n -= 1
total = 0
for i in range(0,len(list)):
    if list[i] == ".":
        continue
    total += i * int(list[i])
print(list)
print(total)
