sc = input("Score: ")
try:
    sc = float(sc)
except:
    print("Bad Score")
if sc >= 1.0:
    print("Bad Score")
else:
    if sc >= 0.9:
        print("A")
    elif sc >= 0.8:
        print("B")
    elif sc >= 0.7:
        print("C")
    elif sc >= 0.6:
        print("D")
    else:
        print("F")