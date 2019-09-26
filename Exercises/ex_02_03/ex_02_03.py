sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

if fh>40 :
    # regional time x 1 + overtime x 0.5
    xp = (fh * fr) + ((fh-40) * (fr * 0.5))
else :
    # regional time x 1
    xp = (fh * fr)
print("Pay:",xp)
