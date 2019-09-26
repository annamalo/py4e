
import urllib.request
fname = input('Enter an URL: ')

try:
    fhand = urllib.request.urlopen(fname)
except:
    print('Page cannot be opened:', fname)
    exit()

count = 0
total_count = 0

for line in fhand:
    words = line.decode().split()
    for x in words:
        word = x
        for y in word:
            total_count = total_count + 1
            if count < 3000 :
                count = count + 1
                print(y, end='')
        print(" ", end='')
    print(" ")

print('\n''Total characters in document: ', total_count, '\n''Total characters printed: ', count, '\n''Characters left to 3000: ', 3000-count)
