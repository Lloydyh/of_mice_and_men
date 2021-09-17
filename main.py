#UNFINISHED WORK


import time
import random

print ("Welcome to Mice & Men!")
instructionsanswer = input ("Would you like to see some instructions, y/n: ")
if instructionsanswer == "y":
    print ("""
    The game works like this:
    The computer will randomly generate a 4-digit number.
    It will then ask you to guess the 4-digit number. For every digit that you guessed correctly in the correct place, you have a “mouse”.
    For every digit you guessed correctly in the wrong place is a “man”
    Once the user guesses the correct number, the game is over.
    """)
    input ("Press enter when you are ready to continue...")
else:
    print ("GOOD LUCK!!!!")
    
randomnumber = random.randint(1000,9999)
numberofmice = 0
numberofmen = 0
numberofattempts = 0
gameloop = True

while gameloop == True:
    print (randomnumber)
    userinput = int(input ("Type in what you think the 4-digit number is: "))
    if userinput == randomnumber:
        numberofattempts = numberofattempts+1
        gameloop = False
    else:
        for number in str(userinput):
            if number in str(randomnumber):
                numberofmen = numberofmen+1
            
        
        
print ("Well Done! You have completed the game!")
print (f"It took {numberofattempts} attempts to get the number, which was {randomnumber}")