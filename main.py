#Here we are going to design a number guessing application
#where user is going to guess the number between the given range

#we will be using random maodule to generate the random number
import random as rand

def generateRandomNumber():
    try:
        #prompting the user to give the start and end point of the range
        start=eval(input("Enter the starting point of the range"))
        end=eval(input("Enter the End point of the range"))
    except ValueError:
        print("If u are taking neagtive Range value !!! please make sure to take start and end value properly according to negative number system.")
    random=rand.randint(start,end)
    # print(random)
    return random
def gues():
    count=0
    random=generateRandomNumber()
    while True:
        count=count+1
        guess=eval(input("Please Enter your {} attempt".format(count)))
        if guess==random:
            print("Congratulation u guessed the number correctly!!")
            print("Your number is {}".format(guess))
            print("You take {} times to guess the number".format(count))
            break
        if(random>guess ):
            print("Your Guessed Number is less than number !!! keep trying ")
            continue
        else:
            print("You are greater than the Number !!! keep trying")
            continue           
gues()