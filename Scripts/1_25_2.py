import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_1_25.txt"), 'r')
sum = 0
current_loc = 50
while True:
    line = f.readline()
    if not line:
        break
    dir = line[0]
    line = int(line[1:-1])
    if dir == 'L':
        val = current_loc-line
        if current_loc == 0:
            current_loc = val % 100
            sum += int(abs(val / 100))
        elif val <= 0:
            current_loc = val%100
            sum += int(abs(val / 100))+1
        else:
            current_loc = val

    if dir == 'R':
        val = current_loc+line
        if val >= 100:
            current_loc = val%100
            sum += int(abs(val / 100))
        else:
            current_loc = val


    print(current_loc)
    print(sum)

