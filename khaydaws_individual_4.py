#khaydaws
#Group 4
#Homework 4

#1) %m is the placeholder that shows the month as a three letter abbreviation


#2) Shop Records Algorithm


#1. Import csv and datetime
#a)Create a string called "Friday"
##2. Open csv file in DictReader
##3. Create a variable shop_data  to read the file
##4. Read each line in row object.
##a. Search for Friday in each line.
##b. If (4.a) is TRUE, Print row[1], which is item name.
##5. Repeat step 4 until all lines are read.
##6. Exit.

#3) Shop Records Program

import csv


shop_data = csv.DictReader(open("ShopRecords.csv" , "r"))


for row in shop_data:
    if fri in row:
        print (row[1])

