#Grade calculator - calculate a Grade A,B,C,D,E,F based on numeric score

score = int(input("Enter num1\n"))

if (score >= 91) and (score <= 100):  # simplified chaining format --> 90 <=score  <=100
    print("YOUR SCORE: \t", score, "\n YOUR GRADE : \t A")
elif (score >= 81) and (score >= 90):
    print("SCore", score, "GRADE : \t B ")
elif (score >= 71) and (score >= 80):
    print("SCore", score, "GRADE : \t C")
elif (score >= 61) and (score >= 70):
    print("SCore", score, "GRADE : \t D")
elif (score >= 51) and (score >= 60):
    print("SCore", score, "GRADE : \t E")
else:
    print("SCore", score, "GRADE : \t F")
