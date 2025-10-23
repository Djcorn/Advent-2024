import pathlib
import numpy
import copy

f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_12_24.txt"), 'r')
lines = []
checked = set([])
total = 0
area = 1
perimeter = 0
while True:
    line = f.readline()
    if not line:
        break
    line = list(line[:-1])
    lines.append(line)
print(lines)
stack = []
rows = 3
cols = 4

#perm = numpy.full((rows, cols), initial_value)
# Creates a 2D list where each element is 'initial_value'
def find_path(x,y, target, dir):
    global area
    global perimeter
    while dir > 0:
        if x>0 and lines[x - 1][y] == target and dir==4 and (x-1, y) not in checked:
            stack.append((x, y, target, 3))
            area += 1
            checked.add((x, y))
            perm_check.add((x, y))
            x -= 1
        elif y<=138 and lines[x][y + 1] == target and dir>=3 and (x, y+1) not in checked:
            stack.append((x, y, target,2))
            area += 1
            checked.add((x, y))
            perm_check.add((x, y))
            y += 1
        elif x<=138 and lines[x + 1][y] == target and dir>=2 and (x+1, y) not in checked:
            stack.append((x, y, target,1))
            area += 1
            checked.add((x, y))
            perm_check.add((x, y))
            x += 1
        elif y>0 and lines[x][y - 1] == target and dir>=1 and (x, y-1) not in checked:
            area += 1
            checked.add((x, y))
            perm_check.add((x, y))
            y -= 1
        else:
            checked.add((x, y))
            perm_check.add((x, y))
            if len(stack) == 0:
                return
            else:
                find_path(*stack.pop())
                return
        dir = 4
def find_perm(perm_check):
    total = 0
    for i in perm_check:
        temp = 4
        if (i[0]-1,i[1]) in perm_check:
            temp-=1
        if (i[0]+1,i[1]) in perm_check:
            temp-=1
        if (i[0],i[1]-1) in perm_check:
            temp-=1
        if (i[0],i[1]+1) in perm_check:
            temp-=1
        total +=temp
    return total
for i in range(0,140):
    for j in range(0,140):
        if  (i, j) not in checked:
            perm_check = set([])
            target = lines[i][j]
            dir = 4
            print(target)
            find_path(i,j,target,dir)
            perimeter = find_perm(perm_check)
            print("area " + str(area))
            print("perimeter " + str(perimeter))
            total += area * perimeter
            area = 1
            perimeter = 0
print("total " + str(total))