fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

domain = []
counts = {}

# break each line into a list of words
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From' : continue
# add all emails to a list
    email = words[1]
# find the @ position and ad whats after the @ sign to a domain variable
    at = email.find('@')
    domain = email[at+1:]
# count each domain using counts dictionary
    counts[domain] = counts.get(domain,0)+1

# print(counts) prettier
for k,v in counts.items():
    print(k,v)
