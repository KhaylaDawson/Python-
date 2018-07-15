#Khayla Dawson
#khaydaws
#Group 4
#Homework 1

#Rock, Paper, Scissors Algorithm

#1) Have a user enter in rock, paper, or scissors and save it to a variable

#2) Create a list of rock, paper, or scissors so that the computer will choose one of
#   those objects from the list randomly

#3) Import the function random so that the computer will choose randomly of the 3 objects

#4) Set the conditions of rock, paper, scissors
#   so that Rock beats Scissors, Paper beats rock, and Scissors beats paper

#5) Do this by creating boolean conditions that compares what the computer chose and what the user chose
#   in the range of (0,2) from the list that contains the objects

#6) Call for the function outside of the definition
#   Inside of the main code 

#7) Run the code 
#8) Tell the user if they either won, lost, or tied based on the comparison


#Rock, Paper, Scissors Game!

import random

def rock_paper_scissors():
    user_choice = input("Rock, paper or scissor?: ")
    computer_choices = ["rock", "paper", "scissor"]
    random_choice = random.randint(0, 2)

    if computer_choices[random_choice] == "rock" and user_choice == "scissor":
        print("Computer won with rock.")
    elif computer_choices[random_choice] == "scissor" and user_choice == "paper":
         print("Computer won with scissor.")
    elif computer_choices[random_choice] == "paper" and user_choice == "rock":
        print("Computer won with paper.")

    elif computer_choices[random_choice] == "scissor" and user_choice == "rock":
        print("You won with rock.")
    elif computer_choices[random_choice] == "paper" and user_choice == "scissor":
        print("You won with scissor.")
    elif computer_choices[random_choice] == "rock" and user_choice == "paper":
        print("You won with paper.")

    else:
        print("It's a tie! Play again")
###main
rock_paper_scissors()


#Reverse String Program

#Defined function that will reverse the characters in a string
def reverse(string):
    #Create empty list that will be called on later in the function
    return_string = []

    #For loop will loop through each character from index 0 to the length of the string
    for char in range(0, len(string)):
        return_string.append(str(string[len(string) - char - 1]))

    
    print(''.join(return_string))

#The function will ask the user to input a string
#so that the characters will be reversed
reverse(input("Enter a string: "))


#Abbreviation Function

#Dictionary of the weekdays along with their one letter abbreviation
weekdays = {"M": "Monday","T": "Tuesday","W": "Wednesday","R": "Thursday","F": "Friday","S": "Saturday","U": "Sunday"}

#Define function that will take a string and return its abbreviation
def fullweek(abbrev_string):
    #Create boolean condition so that the function will return the abbreveation
    #If the abbrevetiation isn't a weekday it will return "Not a weekday"

    if abbrev_string in weekdays:
        return weekdays[abbrev_string]

    else:

        return "Not a weekday"
