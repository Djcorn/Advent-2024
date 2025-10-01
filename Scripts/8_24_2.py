import pathlib
import numpy
import copy
f = open(pathlib.Path(r"C:\\Users\cornelld\Advent\Inputs\input_8_24.txt"), 'r')
lines = []
totals = 0
while True:
    line = f.readline()
    if not line:
        break
    lines.append(line[:-1])
locations = copy.deepcopy(lines)
x = type(locations)
for i in range(0,len(locations)):
    locations[i] = list(locations[i])
characters = []
for row_index, row in enumerate(lines):
    for col_index, char in enumerate(row):
        if char != ".":
            characters.append([row_index, col_index, char])

for i in range(0,len(characters)):
    for j in range (i+1, len(characters)):
        if characters[i][2] == characters[j][2]:
            y1 = characters[i][1] + (characters[i][1] - characters[j][1])
            y2 = characters[j][1] + (characters[j][1] - characters[i][1])
            x1 = characters[i][0] + (characters[i][0] - characters[j][0])
            x2 = characters[j][0] + (characters[j][0] - characters[i][0])
            while 0 <= x1 < 50 and 0 <= y1 < 50:
                locations[x1][y1] = '#'
                y1 += (characters[i][1] - characters[j][1])
                x1 += (characters[i][0] - characters[j][0])
            while 0 <= x2 < 50 and 0 <= y2 < 50:
                locations[x2][y2] = '#'
                y2 += (characters[j][1] - characters[i][1])
                x2 += (characters[j][0] - characters[i][0])

for row in locations:
    for column in row:
        if column != ".":
            totals+=1
            print(totals)

print(characters)
print(lines)
print(locations)