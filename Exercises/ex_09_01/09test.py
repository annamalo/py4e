fhand = open('words.txt')
keys = {}


for line in fhand:
    words = line.split()
    for word in words:
        if word not in keys:
            keys[word] = 1
        else:
            keys[word] += 1

print(keys)


for line in fhand:
    words = line.split()
    for word in words:
        keys.get(word, 0)

print(keys)
