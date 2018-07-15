##def fact_1_function(num):
##    if num == 1:
##        return 1
##    else:
##        return fact_1_function(num -1) * num
##
##print(fact_1_function(994))



##def add_0_function(num):
##    if num == 0 or num == 1:
##        return 1 
##    else:
##        return add_0_function(num -1) + add_0_function(num -2)
##
##print(add_0_function(15))
##
##for i in range(50):
##    print(add_0_function(i))



class Puppy(object):
    names = {}

    @staticmethod
    def dog_names():
         table_print(("Name", "Times"), sorted(Puppy.dog_names.items()), 7)


    def __init__(self, name):
        
        self.__name = name
        self.__bark_counter = 0
##        if name in Puppy.dog_names:
##            Puppy.dog_names[name] += 1
##        else:
##            Puppy.dog_names[name] = 1
        

    def bark(self):

        self.__bark_counter += 1
        print("Bark!")
        print(self.__name, "has barked", self.__bark_counter, "time(s). \n")

        
    def __str__(self):
        reply = "\nPuppy object\n"
        reply += "Name: " + self.__name + "\n"
        reply += "Bark Counter: "
        reply += str(self.__bark_counter) + "\n"
        return reply

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            print("The name has been changed.")
        else:
            print("The name cannot be an empty string")
        

puppy = Puppy("Spot")

puppy.set_name("")
print(puppy.get_name())
puppy.set_name("Rex")
print(puppy.get_name())


##puppy2 = Puppy("Spot")
##puppy3 = Puppy("Rover")
##puppy4 = Puppy("Rover")
##puppy5 = Puppy("Rover")
##puppy6 = Puppy("Lassie")
##
##Puppy.dog_names()

##for i in range(5):
##    puppy.bark()

##print(puppy)
##print(puppy2)
##print(puppy3)
##    
