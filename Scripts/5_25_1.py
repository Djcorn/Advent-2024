import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_5_25.txt"), 'r')
sum = 0
fresh_array =[]
while True:
    line = f.readline()
    line = line[:-1]
    if not line:
        break
    line = line.split('-')
    fresh_array.append(int(line[0]))
    fresh_array.append(int(line[1]))
    print(line)
print(fresh_array)
while True:
    line = f.readline()
    if not line:
        break
    line = int(line[:-1])
    for i in range(0,len(fresh_array)-1,2):
        if line >= fresh_array[i] and line <= fresh_array[i+1]:
            print("fresh")
            sum+=1
            break

    print(line)

print(sum)