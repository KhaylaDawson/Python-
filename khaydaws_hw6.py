##
###6.20
##
##phonebook = {
##     "Smith, Jane" : "123-45-67",
##     "Baker, David" : "987-65-43",
##     "Doe, John" : "567-89-01"
##     }
##            
##def reverse(phonebook):
##    returnDict = {}
##    for key, value in phonebook.items():
##        returnDict[value] = key
##    return returnDict
##
##print(reverse(phonebook))


#6.22

##nonReverseLetters = ["a", "e"]

##ReverseLetters = [
##def mirror(string):
##    returnWord = ""
##    for number in range(len(string)):
##        if string[len(string)-number-1] == "b":
##            returnWord+="d"
##        elif string[len(string)-number-1] == "d":
##            returnWord+="b"
##        elif string[len(string)-number-1] in ReverseLetters:
##            return "INVALID"
##        else:
##            returnWord+=string[len(string)-number-1]
##    return returnWord
##
##print(mirror("vow"))
##print(mirror("wood"))
##print(mirror("bed"))
##                
##            
##

##reverseLetters = ["b", "d", "i", "l", "w", "v", "o", "u", "p", "q"]
##
##def mirror(string):
##   mirrors = {"v : b", 
##            
            







##
##6.24
##
##def names():
##    newDict = {}
##
##    while True:
##        newName = input("Enter the next name: ")
##        if newName == "":
##            break
##        elif newName in newDict:
##            newDict[newName] = newDict[newName] + 1
##        else:
##            newDict[newName] = 1
##    for key, value in newDict.items():
##        if value == 1:
##            print("There is 1 student named",key)
##        else:
##            print("There are "+str(value)+" named "+key)
##names()
##

#6.28

##def translate(phrase):
##    translationDict = {
##        "hello":"Hola",
##        "everyone": "Todos"
##    }
##    returnString = ""
##    phraseList = phrase.split(" ")
##    for word in phraseList:
##        if word in translationDict.keys():
##            returnString += translationDict[word]+ " "
##        else:
##            returnString += "----"
##
##    return returnString
##
##print(translate(input(str("Enter a phrase to be translated: "))))
##

##6.33

##import random
##
##def diceprob(r):
##    count_roll = 0
##    count_match = 0
##    
##    while count_match <= 100:
##        count_roll += 1
##        roll_v = random.randrange(2, 13)
##        if roll_v == r:
##            count_match += 1
##        
##
##
##    print(" It took " + str(count_roll) + " to get 100 rolls of " + str(r))
##              
##    
##
##    
    

