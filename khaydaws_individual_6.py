#Khayla Dawson
#Group 4
#Homework 6
#khaydaws


#Display Book Algorithm

#Import xml etree module for element tree
#Create function display_bok(id)

#Set root of tree as an variable to library.xml file
#Set where to start from in the file (book section)
#Write for loop to go over every book in section
#Create if statement (if book.attrib) of function being equal
#to the attribute of book(if statement), put the information into the variable
#Return info
#Return not found if nothing is equivalent


import xml.etree.ElementTree as ET


def display_book(id):


    root = ET.parse(source="library.xml")
    
    books = root.iter("book")
    
    for book in books:
    
        if book.attrib == {'id' : id}:
        
            title = book.find("title")
            author = book.find("author")
            price = book.find("price")
            print("Title: ",title.text,"\n", "Author: ", author.text, "\n", "Price: ", price.text)
            print("-"*30)
##          info = book.find("title").text + "; " + book.find("author").text + "; " + book.find("price").text
##          return id
##
##    return "Not Found" #(sidenote - the return is not working so I commented it out)

    #Use findall to make a list of everything that is found in section (because it should be multiple of results I want)
    #Set variables for all of the information that I need
    #Create for loop to go thorugh the section to find the "computer" book released in "December"
    #Set range of lenth of everything in list that is formed with books that qualifies my criteria
    #Create If statement; if the book is published on December (use index, because it is a list)
    #Print the results
    
    published = root.findall("book/publish_date")
    author = root.findall("book/author")
    title = root.findall("book/title")
    price = root.findall("book/price")
    
    
    for i in range(len(published)):
        
        
        if published[i].text.split("-")[1] == "12":
            
            print("Author: ", author[i].text)
            print("Title: ", title[i].text)
            print("Price: ", price[i].text)
            
            
    print("-"*30)

   
    #Find every genre of the book, need to use findall since it could be multiple of it
    #Use for loop to go through every genre in section
    

    genres =root.findall("book/genre")
    
    
    for genre in genres:
       print(genre.text)

display_book("bk107")




