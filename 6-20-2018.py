###Building a List Comprehension
##
###The result will be a list
###Add in brackets
##result_list = []
##
###Put in iteration and a base output
###The iteration is the for loop
###The output is x
##result_list = [x for x in range(10)]
##
###Add in the logic
###Which is to square the value of every number met
###While looping through the "orginal list"
##result_list = [x**2 for x in range(10)]
##
###Can add conditions
##set_b = []
##for i in range(1,20):
##    if i % 2 == 0:
##        set_b.append(i)
##
###To simplify the code to a single line
###The condition could be we written as
##set_b = [i for i in range(1,20) if i % 2 == 0]
##
##
##
###Call for a function
##def squares(num):
##    squares = [num**num for num in range(num+1)]
##    return squares
##
##
###main
##print(squares(10))


##doubles = [x * 2 for x in range(10)]


##upper_bound = eval(input("Please enter a lower bound(int): ") 
##
##lower_bound = eval(input("Please enter an upper bound(int): ")
##
##evens = [print("All of the even numbers between") for i in range(lower_bound,upper_bound)]
##
##evens_div
##
##
##file_name = input("Please enter a file name: ")
##print("All words in the file: ")
##words_contents = [line.strip() for line in open("words.txt", "r")]
##print (words_contents)
##
##
####
####def vowel_count(word):
##    count = 0
##    for letter in word:
##        if letter in "aeiou":
##            count += 1
##
##
##    if count >= 2:
##        return True
##    else:
##        return False
##    
##vowels = [word for word in words_contents if vowel_count(word)]
##
##print("The words in the file that contain 2 or more vowels: ", vowels)
##

##words = ["apple", "ball", "candle", "dog", "Egg", "frog"]
##words = [word.upper() if words[i].upper(words) <= 4 for word in words(len(words))]
##words = result
                    

secret = input("Please enter the secret: ")
secret_message = ["-" if  letter.isalpha() else letter for letter in secret]
print("".join(secret_message))
