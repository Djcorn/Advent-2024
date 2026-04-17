import math
import pathlib
import numpy

f = open(pathlib.Path(r"C:\\Users\cornelld\Documents\Advent-2024\Inputs\input_8_25.txt"), 'r')
sum = 0
fresh_array = []
while True:
    line = f.readline()
    line = line[:-1]
    if not line:
        break
    line =line.split(',')

    fresh_array.append([float(item) for item in line])

new_list = []
connected = [False]*len(fresh_array)
shortest_list= []

def func():
    shortest = 1000000000
    shortest_1 = 0
    shortest_2 = 0
    for i in range(0,len(fresh_array)):
        for j in range(i+1,len(fresh_array)):
            dist = math.sqrt(
                             ((fresh_array[i][0]-fresh_array[j][0])**2)+
                             ((fresh_array[i][1]-fresh_array[j][1])**2)+
                             ((fresh_array[i][2]-fresh_array[j][2])**2)
                             )
            if dist < shortest :
                if dist in shortest_list:
                    continue
                else:
                    shortest = dist
                    shortest_1 = i
                    shortest_2 = j


    shortest_list.append(shortest)
    if connected[shortest_1] and connected[shortest_2]:
        for t in new_list:
            if t.__contains__(fresh_array[shortest_1]) and t.__contains__(fresh_array[shortest_2]):
                return
    if connected[shortest_1] and connected[shortest_2]:
        for i in range(0,len(new_list)):
            if new_list[i].__contains__(fresh_array[shortest_1]) :
                index1 = i
            if new_list[i].__contains__(fresh_array[shortest_2]):
                index2 = i
        for i in new_list[index2]:
            new_list[index1].append(i)
        new_list.pop(index2)

    elif connected[shortest_1]:
        for i in new_list:
            if i.__contains__(fresh_array[shortest_1]):
                new_list[new_list.index(i)].append(fresh_array[shortest_2])
    elif connected[shortest_2]:
        for i in new_list:
            if i.__contains__(fresh_array[shortest_2]):
                new_list[new_list.index(i)].append(fresh_array[shortest_1])
    else:
        new_list.append([fresh_array[shortest_1], fresh_array[shortest_2]])



    connected[shortest_1] = True
    connected[shortest_2] = True

for x in range(0,1000):
    func()
for x in range(0,3):
    highest = 0
    highest_index = 0
    for i in range(0,len(new_list)):
        length = len(new_list[i])
        if length > highest:
            highest = length
            highest_index = i
    new_list.pop(highest_index)
    print(highest)
