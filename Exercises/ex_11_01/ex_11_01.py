import re

fname = ('mbox-short.txt')
fhand = open(fname)

reg = input("Enter a regular expression: ")

def grep():
    count = 0
    for line in fhand:
        line = line.rstrip()
        if re.search(reg, line):
            count = count + 1
    print(fname, ' had ', count, ' lines that matched ', reg)

grep()
