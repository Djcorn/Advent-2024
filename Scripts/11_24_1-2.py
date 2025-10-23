import pathlib
import numpy
import copy
import tqdm
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_11_24.txt"), 'r')
line = f.readline()
lines = line.split(" ")
for i in tqdm.tqdm(range(0,75)):
    j = 0
    while j < len(lines):
        if int(lines[j]) == 0:
            lines[j] = "1"
        elif len(lines[j])%2==0:
            mid_index = int(len(lines[j])/2)
            front = lines[j][:mid_index]
            back = lines[j][mid_index:]
            lines[j] = front
            lines.insert(j+1,back.lstrip('0'))
            if lines[j+1] == '':
                lines[j + 1] = '0'
            j+=1
        else:
            lines[j] = str(int(lines[j])*2024)
        j+=1
#print(lines)
print(len(lines))