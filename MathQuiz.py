from os import name, system

def clear():
    #Check if the users operating system is windows or not to clear the screen.
    if name == 'nt':
        system('cls')
    else:
        system('clear')

#Dictionary of all of my questions and answers.
questions = {
    "What is 1+1?" : "2",
    "What is the length of the longest side of a right angled triangle if the two shorter sides are 5cm and 12cm?" : "13",
    "What is 5y+5−3y?" : "2y+5y",
    "What is b+b+b+b−b?" : "3b",
    "What is 7x+3+3x?" : "4x+3",
    "What is the square root of 3 to the square root of 2 power times the square root of 3 to the negative square root of 2 power?" : "1",
    "If 1/2x+1/2(1/2x+1/2(1/2x+1/2(1/2x+1/2...=y what does x equal?" : "1",
    "What's the only place in this world who's Fahrenheit and Celsius degrees can be equal?" : "-40",
    "If Alice chooses a = 123 and Bob chooses b = 456 and have agreed on a generator g = 100 in the prime order multiplicative modulo set of p = 2027 calculate the secret key S as per the Diffie-Hellman key exchange algorithm?" : "1929",
    "What are the intergers for x, y, z in x³+y³+z³=42" : "-80538738812075974, 80435758145817515, 12602123297335631"
}

clear()
#Welcoming to the quiz.
input("Beginning of quiz here!\nPress enter to start quiz")


clear()
#This is my variable for the score.
currentScore = 0

#This is the the code that goes through each question and answer in my dictionary.
for q in questions:
    print("Current score: ", currentScore)
    answer = input(q + "\n")
    if answer == questions[q]:
        input("Answer correct!")
        #This is how the users score increases when they get an answer correct.
        currentScore = currentScore + 1
    else:
        input("Incorrect!")
    clear()
#This prints a message at the end of the quiz with the users score.
print("Congratulations! You scored ", currentScore, " out of ", len(questions))
input()