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






"""

#setting up variables which will but used to fill in equations. Random will be imported here
import random
A = random.randrange(1,100)
B = random.randrange(1,100)
C = random.randrange(1,100)

#Tot will be the user's score. Each question with a correct answer will add 1 to Tot.
#Sofware will keep track of user's score based on Tot
Tot = 0

#setting up equations, using A/B/C with the random assigned numbers

#Q1
print("Question 1: x = (" + str(A) + " + " + str(B) + ") * " + str(C))
ans1 = int(input("x = "))
q1 = (A + B)*C 

if ans1 == q1:
    print("Your answer is correct!")
    Tot = Tot + 1
else: 
    print("incorrect! The correct answer is x = " + str(q1))


#Q2
print("Question 2: x = (" + str(B) +  " * " + str(C) + ") / " + str(A))
ans2 = int(input("x = "))
q2 = round((B * C)/A)  # round had to be utilized, since division may not result in an integer

if ans2 == q2:
    print("Your answer is correct!")
    Tot = Tot + 1
else:
    print("incorrect! The correct answer is x = " + str(q2))

#Q3
print("Question 3: x = (" + str(C) +  " * " + str(A) + ") / " + str(A))
ans3 = int(input("x = "))
q3 = (C*A)/A #round will not be needed here, as A will be canceled out (A/A)

if ans3==q3:
    print("Your answer is correct!")
    Tot = Tot + 1
else:
    q3 = int(q3) #q3 must be converted into "int" so answer is not displayed as float due to division
    print("incorrect! The correct answer is x = " + str(q3))

#Q4
print("Question 4: x = " + str(A) + " + " + str(B) + " + " + str(C))
ans4 = int(input("x = "))
q4 = A+B+C

if ans4==q4:
    print("Your answer is correct!")
    Tot = Tot + 1
else:
    print("incorrect! The correct answer is x = " + str(q4))

#Q5
print("Question 5: x = " + str(A) + " - " + str(B) + " - " + str(C))
ans5 = int(input("x = "))
q5 = A-B-C

if ans5==q5:
    print("Your answer is correct!")
    Tot = Tot + 1
else:
    print("incorrect! The correct answer is x = " + str(q5))

#Q6
print("Question 6: x = " + str(A) + " * " + str(B) + " * " + str(C))
ans6 = int(input("x = "))
q6 = A*B*C

if ans6==q6:
    print("Your answer is correct!")
    Tot = Tot + 1
else:
    print("incorrect! The correct answer is x = " + str(q6))

#Q7
print("Question 7: x = " + str(A) + " / " + str (C))
ans7 = int(input("x = "))
q7 = round(A/C)

if ans7 == q7:
    print("Your answer is correct!")
    Tot = Tot + 1
else:
    print("incorrect! The correct answer is x = " + str(q7))

#Q8
print("Question 8: x = " + str(A) + " * " + str (B))
ans8 = int(input("x = "))
q8 = A*B

if ans8 == q8:
    print("Your answer is correct!")
    Tot = Tot + 1
else:
    print("incorrect! The correct answer is x = " + str(q8))

#Q9
print("Question 9: x = ((" + str(A) + " + " + str(B) + ") * " + str(C) + ") * " + str(A))
ans9 = int(input("x = "))
q9 = ((A + B)*C)*A

if ans9 == q9:
    print("Your answer is correct!")
    Tot = Tot + 1
else: 
    print("incorrect! The correct answer is x = " + str(q9))

#Q10
print("Question 10: x = ((" + str(A) + " + " + str(B) + ") * " + str(C) + ") / " + str(A))
ans10 = int(input("x = "))
q10 = round(((A + B)*C)/A)

if ans10 == q10:
    print("Your answer is correct!")
    Tot = Tot + 1
else:
    q10 = int(q10)
    print("incorrect! The correct answer is x = " + str(q10))


print(str(name) + ",")

if Tot >= 7:
    print("Congratulations, you passed!")
    print("You correctly aswered " + str(Tot) + " out of 10 questions!")
elif Tot < 7:
    print("You failed!")
    print("You correctly aswered " + str(Tot) + " out of 10 questions!")
"""