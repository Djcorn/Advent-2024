import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_2_25.txt"), 'r')
sum = 0

line = f.readline()
list = line.split(",")
for item in list:
    bounds = item.split("-")
    for i in range(int(bounds[0]),int(bounds[1])+1):
        string_i = str(i)
        for j in range (1,int(len(string_i)/2)+1):
            split_string_list = [string_i[x:x + j] for x in range(0, len(string_i), j)]
            if(len(set(split_string_list)) == 1):
                sum += i
                break
print(sum)
