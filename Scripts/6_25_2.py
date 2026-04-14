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
    fresh_array.append(list(line))
transposed = np.array(fresh_array).T

while len(transposed)>0:
    new_array = []
    for i in transposed:
        if all(x == ' ' for x in i):
            transposed = np.delete(transposed, 0,axis=0)
            break
        else:
            new_array.append(i)
            transposed = np.delete(transposed, 0, axis=0)
    var = new_array[0][len(new_array[0])-1]
    total = 0
    if var == '+':
        for i in new_array:
            string = ""
            for j in range(0,len(i)-1):
                if i[j] != '' or i[j] != ' ' or i[j] != '*' or i[j] != '+':
                    string += i[j]
            value = int(string)
            if var == '+':
                total += value
    if var == '*':
        for i in new_array:
            string = ""
            for j in range(0,len(i)-1):
                if i[j] != '' or i[j] != ' ' or i[j] != '*' or i[j] != '+':
                    string += i[j]
            value = int(string)
            if total != 0:
                total *= value
            else:
                total =value
    final_total += total
print(final_total)