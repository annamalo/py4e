
fname = input('Enter a file name: ')
fhand = open(fname)

count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        col = line.find(':')
        snumber = (line[col+1:])
        fnumber = float(snumber)
        count = count + 1
        total = total + fnumber
print('Average spam confidence: ', total/count)
