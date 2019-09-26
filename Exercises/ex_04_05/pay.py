sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

def computepay(hours,rate):
    if hours>40 :
        # regular time x 1 + overtime x 0.5
        pay = (hours * rate) + ((hours-40) * (rate * 0.5))
    else :
        # regular time x 1
        pay = (hours * rate)
    print(pay)

computepay(fh,fr)
