#Introduction, input to register user's name
print("Welcome to MathWare. This exam will consist of 10 questions. You must get at least 7 correct answers to pass.")
print("Please round your answers so there are no decimals. Half (0.5) will be rounded to the nearest even number.")
name = input("What is your name? ")

import random

def getop():
    op = random.choice("+-/*")
    return op

def getnum():
    num = random.randrange(1,100)
    return num

def math():
    q = 0
    while q <= 10:
        A = getnum()
        B  = getnum()
        C = getnum()
        op1 = getop()
        op2 = getop()
        question = str(A) + op1 + str(B) + op2 + str(C)
        print(question)
        res = round(eval(question))
        print(res)
        ans = int(input("Answer: "))
        while res != ans:
            print("Incorrect, try again!")
            ans = int(input("Answer: "))
        q = q + 1
    print("congrats, you got it all done!")
        
math()