import pathlib
import numpy
f = open(pathlib.Path(r"C:\\Users\cornelld\Advent\Inputs\input_7_24.txt"), 'r')
final_sum = 0
def try_both(items, totals, total):
    i=0
    while items:
        for i in range(0, len(totals)):
            new_sum = totals[i] + items[0]
            new_product = totals[i] * items[0]
            new_concat = int(str(totals[i]) + str(items[0]))
            if new_sum > total:
                new_sum=-1
            if new_product > total:
                new_product = -1
            totals = numpy.append(totals, new_product)
            totals = numpy.append(totals, new_concat)
            totals[i] = new_sum

            if len(items) == 0:
                break
            i+=1
        items = items[1:]
    for item in totals:
        if item == total:
            return item

    return 0
while True:
    line = f.readline()
    if not line:
        break
    items = line.split()
    total = int(items[0][:-1])
    items = items[1:]
    items = [numpy.int64(s) for s in items]

    new_sum = items[0] + items[1]
    new_product = items[0] * items[1]
    new_concat = int(str(items[0]) + str(items[1]))
    items = items[2:]
    totals = [new_sum, new_product, new_concat]
    final_sum += try_both(items, totals, total)

print(final_sum)


