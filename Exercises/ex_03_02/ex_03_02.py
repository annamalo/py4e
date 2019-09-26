sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

if fh>40 :
    # regular time x 1 + overtime x 0.5
    xp = (fh * fr) + ((fh-40) * (fr * 0.5))
else :
    # regular time x 1
    xp = (fh * fr)
print("Pay:",xp)
