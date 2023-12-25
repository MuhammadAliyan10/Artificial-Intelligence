from numpy import random

randomNumber = random.randint(100);
userGuess = int(input("Enter a number between 1 to 100 : "))
guess = 0;

while True:
    if(userGuess > randomNumber):
        userGuess = int(input("The number is greater then the guess number.Try Smaller one : "));
        guess += 1;
    elif (userGuess < randomNumber):
        userGuess = int(input("The number is smaller then the guess number.Try greater one : "));
        guess += 1;
    else:
        guess += 1;
        print("You won the game in " + str(guess) + " guess.")
        break;
    
        
        