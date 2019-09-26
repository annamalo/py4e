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
        print("A")
    elif score >= 0.8 :
        print("B")
    elif score >= 0.7 :
        print("C")
    elif score >= 0.6 :
        print("D")
    else :
        print("F")

computegrade(fscore)
