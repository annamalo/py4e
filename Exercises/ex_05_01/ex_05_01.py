total = 0
count = 0
while True:
    line = input("Enter a number: ")
    if line == "done" :
        break

    try:
        line = int(line)
    except:
        print("Invalid input")
        continue

    total = total + line
    count = count + 1

average = total / count

print(total, count, average)
