
fname = input('Enter a file name: ')
fhand = open(fname)

list_words = []
sorted_list = []

# split into list of words
for line in fhand:
    x = line.split()
    list_words.extend(x)

# check if word is alreadyi in list
for y in list_words:
    if y not in sorted_list:
        sorted_list.append(y)

# sort
sorted_list.sort()
# print
print(sorted_list)
