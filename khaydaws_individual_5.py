#Khayla Dawson
#khaydaws
#Group 4
#Homework 5

#1) The Python regular expression pattern that would match a hex color code is '[\w{6}]'

#2) Men's Basketball Algorithm

#1) Import re, urllib.request to use regular expression and search in url
#2) Open the webpage
#3) Read the webpage, set a variable to save those contents.
#4) Create empty list, 0 number counter
#5) Close the webpage
#6) Use regular expression, re.findall, to find the contents of number of games, score in that contents
#7) Add +1 to win or lose
#8) For those items that I found, make a list of those and print the list

#3) Men's Basketball Program

import re, urllib.request

web_open = urllib.request.urlopen('http://cgi.soic.indiana.edu/~dpierz/mbball.html')

contents = web_open.read().decode(errors = "replace")

web_open.close()

result = []
win = 0
lose = 0

games = re.findall("(?<=div class='schedule_game_results'><div>).*?(?=</div>)", contents)

for i in games:
    if "W" in i:
        win += 1
    elif "L" in i:
        lose += 1
print("Wins: ", win)

print("Losses: ", lose)

points = 0

for game in games:
    if game:
        first_score = game[2:4]
        second_score = game[5:7]
        points += abs(int(first_score) - int(second_score))

print("Total Difference: ", points)
