##import csv
##data = open("people_header.csv", "r")
####people = list(csv.reader(data))
##people = csv.DictReader(open("people_header.csv", "r"))
##for entry in people:
##    print(entry["Name"], "is", entry["Age"], "years old.")
##for line in people:
##    print(line)

import csv

companies = csv.DictReader(open("companies.csv", "r"))
#Indiana_companies = []
user_search = input("Search for companies in what state? " )
print("-" * 40)
#company_nameDict = {}
for entry in companies:
    #if entry["state"] == "IN":
        #Indiana_companies.append(entry["company_name"])
    if entry["state"] == user_search:
      spaces = (40 - len(entry["company_name"])) * " "
      print(entry["company_name"],spaces, entry["web"])
      



#print(sorted(Indiana_companies))
                            

import csv

characters = csv.DictReader(open("starwars.csv", "r"))
print("-" * 40)
print("MAIN CHARACTERS")
print("Star Wars: Episode VII: The Force Awakens (2015)")
print("-" * 40)

    
