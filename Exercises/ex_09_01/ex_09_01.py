fhand = open('words.txt')
keys = {}


for line in fhand:
    words = line.split()
    for word in words:
        keys[word] = 1
# print(keys)

print(keys['continuously'])
print(len(keys))
print('continuously' in keys)
