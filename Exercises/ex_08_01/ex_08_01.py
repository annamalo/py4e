def chop(x):
    del x[0]
    del x[len(x)-1]

def middle(t):
    return t[1:len(t)-1]

firstline = ['zero', 'one', 'two', 'three', 'four', 'five']
print('First line to chop and return None: ', firstline)

delete = chop(firstline)
print(delete)
print('First line after chop: ', firstline)

secondline = ['zero', 'one', 'two', 'three', 'four', 'five']
print('Second line to return middle: ', secondline)

newlist = middle(secondline)
print(newlist)
