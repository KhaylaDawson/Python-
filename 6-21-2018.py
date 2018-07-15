##def vowel_count(line):
##    count = 0
##    for line in line:
##        if line in "aeiou":
##            count += 1
##
##
##    if count >= 2:
##        return True
##    else:
##        return False
##    
##
##file_name = input("Please enter a file name: ")
##print("All lines in the file: ")
##
##line_contents = [line.strip() for line in open("lines.txt", "r")]
##print(line_contents)
##
##vowels = [word for line in line_contents for word in line.split(" ") if vowel_count(word) in line]
##print("The words in the file that contain 2 or more vowels: ", vowels)
##
##


## 
##phraseDict = {"7" : "t","5" : "s","4" : "a", "3": "e","1" : "i"}
##
##user = input("Please enter the phrase to translate: ")
##output = [phraseDict[char] if char in phraseDict else char for char in user]
##print("Output: ", "".join(output))


##num_file = open("100numbers.txt", "r")
##file_contents = num_file.readlines()
##num_file.close()


from string import punctuation

file_contents = [line.strip() for line in open("CaP.txt", "r")]
##for line in file_contents:
##    for word in line:
##        for char in line:
##            if char not in punctuation:
##                words.append
##
file_contents = [char for line in file_contents for char in line if char not in punctuation]


print(file_contents)
