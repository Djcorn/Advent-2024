import pathlib
import numpy
import copy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_10_24_test.txt"), 'r')
lines = []
totals = 0
while True:
    line = f.readline()
    if not line:
        break
    line = list(line[:-1])
    line = [int(s) for s in line]
    lines.append(line)
print(lines)
def find_path(x,y, counter):
    if 0 <= x < 7 and 0 < y < 7:
        if lines[x + 1][y] == counter:
            x += 1
        elif lines[x][y + 1] == counter:
            y += 1
        elif lines[x - 1][y] == counter:
            x -= 1
        elif lines[x][y - 1] == counter:
            y -= 1
        else:
            return
        counter +=1
        if counter == 9:
            global totals
            totals += 1
            return
        find_path(x, y, counter)

    else:
        return

for i in range(0,7):
    for j in range(0,7):
        if lines[i][j]==0:
            counter = 1
            find_path(i,j,counter)
print(totals)