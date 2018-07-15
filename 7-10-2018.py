##out = open("template2.html", "w")
##
##html = """<!doctype html>
##<html>
##<head>
##	<meta charset="utf-8">
##	<title>Google Link</title>
##</head>
##<body>
##	<p>Paragraph 1</p>
##	<p>Paragraph 2</p>
##	<a href="http://www.google.com">This takes you to Google!</a>
##</body>
##</html>"""
##
##out.write(html)
##out.close()
##
##print("Finished writing.")

data = [["Item", "Cost", "Type"], ["Coke", "$2", "Drink"],
["Water", "$0", "Drink"], ["Fries", "$4", "Appetizer"],
["Onion Rings", "$3", "Appetizer"], ["Steak", "$12", "Entree"],
["Chicken", "$8", "Entree"], ["Caesar Salad", "$7", "Entree"]]


out = open("list_to_html", "w")
html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>YO!</title>
</head>
<body>
<table>
    {content}
</table>
</body>    
</html>"""

dataTable = ""
for i in data:
    dataTable += '<tr>'
    for j in i:
        dataTable += '<td>'+str(j)+'</td>'
    dataTable += '</tr>'

out.write(html.format(content=dataTable))
out.close()

##
##import re
##out = open("list_to_html", "w")
##context =
##web_page = urllibrequest



