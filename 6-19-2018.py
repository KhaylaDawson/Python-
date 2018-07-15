##count = 0
###number = input("Please enter a number or STOP: ")
##while True:
##    number = input("Please enter a number or STOP: ")
##    if number.upper() == "STOP":
##        break
##    
##    count += int(number)
##    
##    
##print("The total sum is", count)


#Declare three blank lists
##evens = []
##odds = []
##others = []
##
###Create for loop that will run 10 times
###Get 10 numbers from user
###Sort numbers in list
##
##for i in range(10):
##	user_in = eval(input("Please enter a number: "))
##	
##	if user_in % 2 == 0:
##		evens.append(user_in)
##	elif user_in % 2 == 1:
##		odds.append(user_in)
##	else:
##		other.append(user_in)
##
##print("Evens: ",evens)
##print("Odds: ",odds)
##print("Other: ", others)



##scores = {"Dave": 125, "Abby": 100, "Carrie": 275, "Ben": 150}
##
##print("Current Players:\n" + " ".join(sorted(scores.keys())))
##
##name = input("Please enter a Player Name: ")
##
##print("The score for", name, "is", (scores.get(name, "not found")+"."))


##def valid_pass():
##    while True:
##        password = input("Please enter a password: ")
##
##        if len(password) >= 8:
##            return password
##        else:
##            print("That was not a valid password, please try again")
##
##
###main
##my_password = valid_pass()
##
##print("Your valid password is: ", my_password)
##
##
##def list_count(numbers):
##    numDict = {}
##    for number in numbers:
##        if number in numDict:
##           
##            numDict[number] += 1
##            
##        else:
##            numDict[number] = 1
##
##    return numDict
##
###main
##test1 = [1,1,1,2,2,2,2,2,4,3,3,3,3,3,3]
##print("The list is:", test1)
##print("Number", "Count", sep="\t")
##numDict = list_count(test1)
##for item in numDict.items():
##    print(item[0], item[1], sep = "\t")
##        
     


