fhand = open('mbox-short.txt')

days = []
counts = {}

# break each line into a list of words
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : continue
# add all weekdays to a list
# loop through each of the weekdays in the list
# count each word using counts dictionary
    day = words[2]
    counts[day] = counts.get(day,0)+1

print(counts)

# find the most common day
largest = -1
theword = None
# .items is a method inside of dictionaries that gives the key value pairs, and need two iteration variables
for k,v in counts.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k # capture/remember the word that was largest

print('Most common day: ', theword, ':', largest)
