#.find(query) returns the first sub-element whose tag matches query
#.findall(query) returns a list of all sub-elements whose tag matches query
#query is an element name or path
#To see a dictionary of attributes, call .attrib on the element

import xml.etree.ElementTree as ET


##def fee_find(name):
##     root = ET.parse(source="students.xml")
##     students = root.findall("Student")
##     
##     for student in students:
##        student_name = student.find("name/first").text + " " + student.find("name/last").text
##        if name == student_name:
##            fee = student.find("fees").
##             
##             return name+"owes "+fee.text+" "+fee.attrib["c"
##
##     return "No Body"
##
##print(fee_find("Rose Dawson"))
##print(fee_find("Jack Sparrow"))
##print(fee_find("No Body"))
##

##def id_find(num):
##    root = ET.parse(source="students.xml")
##    students = root.findall("Student")
##    for student in students:
##        if student.find("id").text == num:
##            name = student.find("name/first").text + " " + student.find("name/last").text
##            return name
##
##    return "Not Found"
##            
##
##
##print(id_find("0019846768"))
##print(id_find("0019846789"))
##print(id_find("1234567890"))

    

#root = ET.parse(source="catalog.xml")

#students is the element aka the query
#students = root.iter("Student")
#elements = root.iter()

#for elem in elements:
##    print("Tag Name:", elem.tag)
##    #print("Tag Text:", elem.text)
##    print("Children:", list(elem))
##    print("-" * 20)

##for student in students:
##    print("Student ID:", student.find("id").text, "\n")

##print("The students are")
##for elem in students:
##    first = elem.find("name/first").text
##    last = elem.find("name/last").text
##    print(first, last)
    


##for elem in elements:
##    if elem.attrib:
##        print("Attributes:", elem.attrib)
##        print("-" * 20)



#print(root)
