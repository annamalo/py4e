
import urllib.request
fname = input('Enter an URL: ')

try:
    fhand = urllib.request.urlopen(fname)
except:
    print('Page cannot be opened:', fname)
    exit()

count = 0
total_count = 0
all_text = ''

for line in fhand:
    all_text = all_text + line.decode()

printed_text = all_text[:3000]
total_printed = len(printed_text)
total_count = len(all_text)

print(printed_text)
print('Total characters in document:\t', total_count, '\n''Total characters printed:\t', total_printed, '\n''Characters left to 3000:\t', 3000 - total_printed)
