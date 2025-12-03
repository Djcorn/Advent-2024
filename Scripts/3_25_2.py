import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_3_25.txt"), 'r')
total = 0
def func(line_array, val, highest_index,sum):
    if val == 0:
        return sum
    val -=1
    highest = 1
    for i in range(highest_index, len(line_array)-(val)):
        if line_array[i] > highest:
            highest = line_array[i]
            highest_index = i
    sum = int(str(sum)+str(highest))
    final_val = func(line_array,val,highest_index+1,sum)
    return(final_val)


while True:
    line = f.readline()
    line = line[:-1]
    line_array = [int(char) for char  in line]
    if not line:
        break
    highest_index = 0
    addition = func(line_array,12,highest_index,"")
    print(addition)
    total+=int(addition)

   # val = int(str(first)+str(second))
   # sum += val
print(total)

