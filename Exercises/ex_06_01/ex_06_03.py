def count(word, letter):

    count = 0
    for x in word:
        if  x == letter:
            count = count + 1
    print(count)

count('banana', 'n')
