#import re, urllib.request

##def head_body(url):
##
##    web_page = urllib.request.urlopen(url)
##    lines = web_page.read().decode(errors="replace")
##    web_page.close()
##    head = re.findall('((?<=head>).+?(?=</head>)',lines,re.DOTALL)[0]
##    body = re.findall('((?<=<body extras="searchhere">).+?(?=</body>)', lines, re.DOTALL)[0]
##    return head, body
##            
##                    
###main
##target = input("Searching: ")
##head,body = head_body(target)
##
##print("Head: ", head)
##print("Body: ", body)

import urllib.request,re
import random

def wiki(url):
    web_page = urllib.request.urlopen(url)
    lines = web_page.read().decode(errors="replace")
    web_page.close()
    body = re.findall('(?<=body).+?(?=</body>)',lines,re.DOTALL)[0]
    links = re.findall('(?<=href=").+?(?=")',body)
    wiki_links = [link for link in links if 'wiki' in link if '.org' not in link]
    return wiki_links

#main

user_select = input("Where would you like to start?: ")
wiki_list = wiki(user_select)
jumps = int(input("How many jumps?"))

for i in range(jumps):
    print("Jumping from: ",user_select,"\n")
    jump = random.choice(wiki_list)
    user_select = ("https://en.wikipedia.org/wiki/" + jump)
    print("To: ",user_select)
