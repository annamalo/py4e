sscore = input("Enter score: ")

try:
    fscore = float(sscore)
except:
    print("Bad score")
    quit()

if fscore < 0 or fscore >= 1 :
    print("Bad score")
    quit()

def computegrade(score):
    if score >= 0.9 :
        return"A"
    elif score >= 0.8 :
        return"B"
    elif score >= 0.7 :
        return"C"
    elif score >= 0.6 :
        return"D"
    else :
        return"F"

print(computegrade(fscore))
