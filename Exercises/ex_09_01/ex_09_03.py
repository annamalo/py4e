fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

email = []
counts = {}

# break each line into a list of words
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From' : continue
# add all weekdays to a list
# loop through each of the weekdays in the list
# count each word using counts dictionary
    email = words[1]
    counts[email] = counts.get(email,0)+1

# find the most common day
largest = -1
theword = None
# print(counts) prettier
for k,v in counts.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k

print('Who has the most messages:', theword, 'with', largest, 'messages')
