import pathlib
import numpy as np
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_6_25.txt"), 'r')
sum = 0
fresh_array = []
final_total = 0
while True:
    line = f.readline()
    line = line[:-1]
    if not line:
        break
    array = line.split(' ')
    array = [x for x in array if x != '']
    fresh_array.append(array)

transposed = np.array(fresh_array).T
print(transposed)
for i in transposed:
    var = i[len(i)-1]
    if var == '*':
        total = int(i[0])
        for j in range(1,len(i)-1):
            total *= int(i[j])
        print(total)
    if var == '+':
        total = int(i[0])
        for j in range(1, len(i) - 1):
            total += int(i[j])
        print(total)
    final_total += total
print(final_total)

