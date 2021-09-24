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
numberofattempts = 0
gameloop = True

while gameloop == True:
    print (randomnumber)
    userinput = input ("Type in what you think the 4-digit number is: ")
    if userinput == "STOP":
        print (f"The random number is {randomnumber}")
        exit()
        #userinput = int(userinput)
    if int(userinput) == randomnumber:
        numberofattempts = numberofattempts+1
        gameloop = False
    else:
        numberofmen = 0
        numberofmice = 0
        position = 0
        for number in str(userinput ):
            print (number)
            
            if number == str(randomnumber)[position]:
                numberofmice = numberofmice+1
            else:
                if number in str(randomnumber):
                    ##Work out how random number equals 9955, guess = 5055, answer = 1 men and 2 mice
                        numberofmen = numberofmen+1
            position = position+1
        print (f"You have {numberofmen} men and {numberofmice} mice.")
        numberofattempts = numberofattempts+1
        
print ("Well Done! You got it right!")
print (f"It took {numberofattempts} attempts to get the number, which was {randomnumber}")
