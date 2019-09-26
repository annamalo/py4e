fhand = open('mbox-short.txt')

days = []
counts = {}

# break each line into a list of words
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : continue
# add all weekdays to a list
    days.append(words[2])
# loop through each of the weekdays in the list
for day in days:
# count each word using counts dictionary
    counts[day] = counts.get(day,0)+1

print(counts)
