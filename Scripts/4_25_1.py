import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_4_25.txt"), 'r')
sum = 0
array = []
while True:
    line = f.readline()
    line = line[:-1]
    line_array = [char for char in line]
    array.append(line_array)
    if not line:
        break
array = array[:-1]
for i in range(0,len(array)):
    for j in range(0,len(array[i])):
        local_count = 0
        if array[i][j] == '@':
            if i!=0 and array[i - 1][j]=='@':
                local_count += 1
            if i!=0 and j!=len(array[i])-1 and array[i - 1][j + 1]=='@':
                local_count += 1
            if j!=len(array[i])-1 and array[i][j+1]=='@':
                local_count+=1
            if i!=len(array)-1 and j!=len(array[i])-1 and array[i+1][j+1]=='@':
                local_count+=1
            if i!=len(array)-1 and array[i+1][j]=='@':
                local_count+=1
            if i!=len(array)-1 and j!=0 and array[i+1][j-1]=='@':
                local_count+=1
            if j!=0 and array[i][j-1]=='@':
                local_count+=1
            if  i!=0 and j!=0 and array[i-1][j-1]=='@':
                local_count+=1
            if local_count <4 :
                sum +=1

print(sum)





