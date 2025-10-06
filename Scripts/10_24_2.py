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
stack = []
def find_path(x,y, counter, dir):
    for i in range(0,10):
        if x>0 and lines[x - 1][y] == counter and dir==4:
            stack.append((x, y, counter, 3))
            x -= 1
        elif y<=6 and lines[x][y + 1] == counter and dir>=3:
            stack.append((x, y, counter,2))
            y += 1
        elif x<=6 and lines[x + 1][y] == counter and dir>=2:
            stack.append((x, y, counter,1))
            x += 1
        elif y>=0 and lines[x][y - 1] == counter and dir>=1:
            y -= 1
        else:
            if len(stack) == 0:
                return
            else:
                find_path(*stack.pop())
                return
        if counter == 9:
            global totals
            nines.append((x, y))
            totals += 1


        counter += 1
        dir = 4


for i in range(0,8):
    for j in range(0,8):
        if lines[i][j]==0:
            counter = 1
            dir = 4
            nines = []
            find_path(i,j,counter,dir)
            print(totals)
            totals = 0