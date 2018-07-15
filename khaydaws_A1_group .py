##Khayla Dawson,Jordan Bloom, Yuning Gao
##khaydaws, bloomjor, gao24
##Group 4
##-----------------------------------------------------------------------------------
#Algorithm
#1. import csv and datetime
#2. create a define function to run the 'event' input.
#3. Walk through every row in the dictionary, extract the date without time and remove their slash
#4. Formate the date
#5. If users' events could be find in the dictionary, print out the results
#6. Create another define function
#7. The same step as first define function and is the users' date could be find in the dictionary, print out the results
#8. Use while loop to keep running the questions
#9. Relate users' inputs back to the two define functions.
##------------------------------------------------------------------------------------------------------------------------------
##Importing the necessary modules.
import csv, datetime

##Defining the storm_by_event function.
def storm_by_event(event):
    ##Looping through every storm stored in the storms dictionary.
    for storm in storms:
        ##Storing pieces of the date of the storm to be used in a datetime function.
        year = int(storm["BEGIN_DATE_TIME"][0:9].split("/")[2])
        month = int(storm["BEGIN_DATE_TIME"][0:9].split("/")[0])
        day = int(storm["BEGIN_DATE_TIME"][0:9].split("/")[1])
        ##Storing the datetime date.
        shortDate = datetime.date(year, month, day)
        ##If the event matches the event stored for the storm, print the full description.
        if storm["EVENT_TYPE"] == event:
            print("\n" +"On", shortDate.strftime("%A") + " the " + shortDate.strftime("%d") + " of " + shortDate.strftime("%B"), storm["EPISODE_NARRATIVE"], "This was reported in", storm["CZ_NAME"].title(), "county.", storm["EVENT_NARRATIVE"])
        
##Defining the storm_by_date function.
def storm_by_date(date):
    ##Looping through every storm stored in the storms dictionary.
    for storm in storms:
        ##Storing pieces of the date of the storm to be used in a datetime function.
        year = int(storm["BEGIN_DATE_TIME"][0:9].split("/")[2])
        month = int(storm["BEGIN_DATE_TIME"][0:9].split("/")[0])
        day = int(storm["BEGIN_DATE_TIME"][0:9].split("/")[1])
        ##Storing the datetime date.
        shortDate = datetime.date(year, month, day)
        ##If the datetime matches the date stored for the storm, print the full description.
        if shortDate == date:
            print("\n" +"On", shortDate.strftime("%A") + " the " + shortDate.strftime("%d") + " of " + shortDate.strftime("%B"), storm["EPISODE_NARRATIVE"], "This was reported in", storm["CZ_NAME"].title(), "county.", storm["EVENT_NARRATIVE"])

##Main

##Opening and storing the Indiana_Storms.csv as a dictionary.
storms = csv.DictReader(open("Indiana_Storms.csv", "r"))

##Creating an infinite loop, which the user can break out of by entering a valid selection.
while True:
    ##Asking the user for a selection.
    userSearch = input("Would you like to search by date or by event? ")
    ##If the user inputs date, and a proper date format, store their user inputted date in pieces
    ##to be used in a datetime.date function. Run storm_by_date() with the argument being their date.
    if userSearch.lower() == "date":
        userDate = input("Please enter your date in YYYY/MM/DD format: ")
        userYear = int(userDate.split("/")[0])
        userMonth = int(userDate.split("/")[1] )
        userDay = int(userDate.split("/")[2])
        finalDate = datetime.date(userYear, userMonth, userDay)
        storm_by_date(finalDate)
        break
    ##If the user inputs event, and a proper event, Run storm_by_event() with the argument being
    ##their event.
    elif userSearch.lower() == "event":
        userEvent = input("Please enter the type of weather you are searching for: ")
        storm_by_event(userEvent)
        break
    ##If the user inputs an invalid selection, print a statement saying so.
    else:
        print("That is not a valid selection. Please try again.")

##Additional comments:
##The example output for the bonus is incorrect. 2017/5/15 is a Monday, not a Friday.



    
    
