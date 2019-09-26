fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

time = []
counts = {}

# break each line into a list of words
for line in fhand:
    words = line.split()
    if len(words) < 4 or words[0] != 'From' : continue
# add all timestamps to a list
    time = words[5]
# find the hour position and ad whats after the @ sign to a domain variable
    hour = time[:2]
# count each hour using counts dictionary
    counts[hour] = counts.get(hour,0)+1

# print a sequence sorted by key order by using a for loop
for k, v in sorted(counts.items()):
    print(k, v)
