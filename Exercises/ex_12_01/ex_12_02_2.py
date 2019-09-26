import socket

URL = input('Enter an URL: ')
scount = input('Limit to number of characters: ')
count = int(scount)
count_total = 0

try:
    #find protocol
    dslash = URL.find('//')
    prot = (URL[:dslash+2:])

    #find host, document
    spURL = URL.split('/')
    host = spURL[2]
    doc = spURL[3]
except:
    print('Wrong format:', URL)
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((host, 80))
except:
    print('Page cannot be opened:', URL)
    exit()

gethttp = 'GET '+ URL + ' HTTP/1.0\r\n\r\n'
cmd = gethttp.encode()
mysock.send(cmd)

run = True
while run:
    data = mysock.recv(5120)
    if len(data) < 1: break
    for x in data.decode():
        count = count - 1
        count_total = count_total + 1
        if count < 1:
            run = False
            break
        print(x, end='')

print('\n\n''Characters left: ', count,'\n''Total characters printed: ', count_total)

mysock.close()
