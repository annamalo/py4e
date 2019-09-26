list = []
while True:
    line = input("Enter a number: ")
    if line == "done" :
        break
    try:
        line = int(line)
    except:
        print("Invalid input")
        continue

    list.append(line)

print("Maximum:", max(list))
print("Minimum:", min(list))
