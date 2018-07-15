#Opens up web page
##
##import urllib.request
##
##web_page = urllib.request.urlopen("http://www.soic.indiana.edu/")
##contents = web_page.read().decode(errors="replace")
##web_page.close()
##
##file_out = open("page.html", "w", encoding="utf-8")
##file_out.write(contents)
##file_out.close()
##
##print("All done! Open page.html in your browser! ")
##print(contents)
##
###The os module gets the base file name from a URL
##
##import os
##print("Base:", os.path.basename("http://cgi.soic.indiana.edu/~dpierz/I211/I211Test.html")
##print("Base:", os.path.basename("http://www.cnn.com/"))


##import urllib.request, ssl, os
##
##def getContent(website):
##      print("Attempting to access the page at this URL: ")
##      print(website)
##
##      web_page = urllib.request.urlopen(website)
##      contents = web_page.read().decode(errors="replace")
##      web_page.close()
##
##      basename = os.path.basename(website)
##
##      if basename == '':
##          file_out = open(basename, "w", encoding="utf-8")
##          print("All done! Open", basename, "in your browser!")
##
##      else:
##          file_out = open("index.html","w", encoding="utf-8")
##          print("All done!",os.path.join(os.getcwd(), "in your browser!"))
##
##      file_out.write(contents)
##      file_out.close()
##
###main
##getContent("http://www.razer.com/")
##getContent("http://www.apple.com/")
##                


import re

vowels = "aeiou"
test =
print("Original: ", re.findall(

          
      
      
      
