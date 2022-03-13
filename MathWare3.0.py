#Introduction, input to register user's name
print("Welcome to MathWare. This exam will consist of 10 questions. You must get at least 7 correct answers to pass.")
print("Please round your answers so there are no decimals. Half (0.5) will be rounded to the nearest even number.")
name = input("What is your name? ")

import random

questions = []

def getop():
    op = random.choice("+-/*")
    return op

def getnum():
    num = random.randrange(1,100)
    return num

def math():
    q = 1
    pts = 0
    s = 1
    while q <= 10:
        A = getnum()
        B  = getnum()
        C = getnum()
        op1 = getop()
        op2 = getop()
        print("Question " + str(q) + ": ")
        question = str(A) + op1 + str(B) + op2 + str(C)
        print(question)
        res = round(eval(question))
        print(res)
        ans = int(input("Answer: "))
        if res == ans:
            pts = pts + 1
        q = q + 1
        tup = (question, res, ans)
        questions.append(tup)
        print("\t")
    
    print("You scored " + str(pts) + " out of " + str(q-1) + "!")
    print("\t")

    while s <= 10:
        for x in questions:
            print("Question " + str(s) + ":")
            (question, res, ans) = x
            print(question)
            print("Correct Answer: ")
            print(res)
            print("Your Answer:")
            print(ans)
            s = s + 1
            print("\t")


    print("congrats, you got it all done!")
        
math()

