
print("~~~~~NUMBER GUESSING GAME~~~~~~")
import random
Mynumber=random.randrange(1,100)
print("I have a number in my mind.Can you guess it !!!")

while True:
    guess=int(input("Enter Your Guess:"))

    if(Mynumber==guess):
        print("Yess you are Right!!!")
        break
    elif(Mynumber>guess):
        print("My Number is greater than the number you guessed!!! TRY AGAIN!!!",end="\n\n")
    else:
        print("My Number is smaller than the number you guessed!!! TRY AGAIN!!!",end="\n\n")
