import urllib.request, ssl, os, re

context = ssl._create_unverified_context()

web_page = urllib.request.urlopen("https://en.wikipedia.org/wiki/2017_in_film", context=context)
contents = web_page.read().decode(errors="replace")
web_page.close()

table = re.findall('(?<=<caption>Highest-grossing films of 2017</caption>).+?(?=</table>)', contents, re.DOTALL)[0]
movieLinks = re.findall('(?<=<td><i><a href=").+?(?=")', table)
linkList = [link for link in movieLinks if 'wiki' in link if '.org' not in link]


print("-"*40)
print("Wiki links for top 10 grossing films in 2017:")
print("-"*40)
for link in linkList:
    print(link)
    print("-"*40)

##Part 2

userMovie = input("Please select a top 10 movie: ")
web_page = urllib.request.urlopen("https://en.wikipedia.org/wiki/" + userMovie, context=context)
movieContents = web_page.read().decode(errors="replace")
web_page.close()

moviePlot = re.findall('(?<=title="Edit section: Plot">edit</a>).+?(?=<h2>)', movieContents, re.DOTALL)[0]
print(moviePlot)


##Part 3

for i in range:
