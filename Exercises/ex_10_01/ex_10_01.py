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

print('*** print the dictionary ***')
# print the dictionary
print(counts)

print('*** print the list of (key, value) tuples ***')
# print the list of (key, value) tuples
print(counts.items())

print('*** print a sorted list of tuples (a sorted version of the dictionary) ***')
# print a sorted list of tuples (a sorted version of the dictionary)
t = sorted(counts.items())
print(t)

print('*** print a sequence sorted by key order by using a for loop ***')
# print a sequence sorted by key order by using a for loop
for k, v in sorted(counts.items()):
    print(k, v)

print('*** print a sequence sorted by value order by constructing a list of (value, key) ***')
# print a sequence sorted by value order by constructing a list of (value, key)
l = []
for k, v in counts.items():
    l.append((v, k))
for v, k in sorted(l, reverse=True):
    print(v,k)

# find the most common day
largest = -1
theword = None
# print(counts) prettier
for k,v in counts.items():
    if v > largest:
        largest = v
        theword = k

print('*** Who has the most messages:', theword, 'with', largest, 'messages ***')
