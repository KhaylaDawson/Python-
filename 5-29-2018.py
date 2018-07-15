####us_coins = {"quarter": "25"}
####
####key = word value = count of word
####
####key = nicknames value = full names
####
##
####text_file = open("INCounties2015.txt", "r")
####
####file_contents = text_file.readlines()
####
####text_file.close()
####
####counties_data = {}
####
####for string in file_contents:
####   county_data = string.strip().split("\t ")
####   counties_data[county_data[0]] = int(county_data[1].replace(",", "" ))
##
####print(counties_data)
##
####counties = ", ".join(counties_data.keys())
####print(counties)   
####print("The population of Monroe County as of 2015 was", counties_data["Monroe"])
####print("The total IN population as of 2015 was", sum(counties_data.values()))
####print("So Monroe County accounts for", counties_data["Monroe"]/sum(counties_data.values())*100, "% of IN's population")
####
####
####text_file = open("top100moviesAFI.txt", "r")
####file_contents = text_file.readlines()
####text_file.close()
####
####AFI_movies = set(file_contents)
####
######print(AFI_movies)
####
####
####
######movies = open("top100moviesRT.txt", "r")
####
####
####text_file = open("top100moviesRT.txt", "r")
####file_contents = text_file.readlines()
####text_file.close()
####
####RT_movies = set(file_contents)
####
######print(RT_movies)
####
####overlap = AFI_movies & RT_movies
####
####for movie in overlap:
####    print(movie.strip())
##
##
##import random
##
##print("Welcome to 'Guess My Number'!")
##print("I'm thinking of a number between 1 and 100.")
##print("Try to guess it in a few attempts as possible")
##
##correct_answer = random.randrange(1, 100)
##
##user_input = int(input("Take a guess: "))
##
##
##
