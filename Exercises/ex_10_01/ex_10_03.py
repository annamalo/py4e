fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

letter = []
counts = {}


# break each line into a list of words
for line in fhand:
    words = line.split()
    # break list of words into words
    for x in words:
        word = x
        # break words into letters
        for letter in word:
            letter = letter.lower()
            # counts frequency of letters a-z
            az = "abcdefghijklmnopqrstuvwxyz"
            if letter in az:
                counts[letter] = counts.get(letter,0)+1

# print counts of letter in order, from most to least common
l = []
for k, v in counts.items():
    l.append((v, k))
for v, k in sorted(l, reverse=True):
    print(k,v)
