import socket

URL = input('Enter an URL: ')

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

count = 300
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    data_decoded = data.decode()
    total_num = len(data_decoded)
    print('Total number of characters in data: ', total_num)
    for x in data_decoded:
        count = count - 1
        if count < 1:
            break
        print(x,end='')
print('Number of characters: ', count)

mysock.close()

# Code: http://www.py4e.com/code3/socket1.py
