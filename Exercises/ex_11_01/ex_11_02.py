import re

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)

    # detta sätt funkar nu
    y = []
    for i in x:
        y.append(int(i))
        for ii in y:
            total = total + ii
            count = count + 1

    # detta sätt funkar
#    old_list = x
#    new_list = [int(i) for i in old_list]
#    for ii in new_list:
#        total = total + ii
#        count = count + 1

print(int(total/count))
