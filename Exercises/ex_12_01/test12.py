
import urllib.request

fname = input('Enter an URL: ')

try:
    fhand = urllib.request.urlopen(fname)
except:
    print('Page cannot be opened:', fname)
    exit()

for line in fhand:
    print(line.decode().strip())
