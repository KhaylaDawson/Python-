class Robot(object):

    robot_list = []

    @staticmethod
    def contenders():
        robots = len(Robot.robot_list)
        print("There are", robots, "robots.\n")
        if robots:
            print("HEre is a list of them:")
        for robot in Robot.robot_list:
            print(robot)



    def __init__(self, name, weapon, rating):
        self.name = name
        self.weapon = weapon
        self.rating = rating
        self.status = True
        print("Robot created!", self.name, "\n")
        Robot.robot_list.append(self)

    def __str__(self):
        reply = "-"*20 + "\n"
        reply += "Fighting Robot \n"
        reply += "Name: " + self.name + "\n"
        reply += "Weapon: " + self.weapon + "\n"
        reply += "Strength: " + str(self.rating) + "\n"
        reply += "Status: "
        if self.status is True:
            reply += "ONLINE \n"
        else:
            reply += "OFFLINE \n"
        reply += "-"*20 + "\n"


        return reply

    



##r2d2 = Robot("R2D2", "Beeps", 2)
##cp30 = Robot("C3PO", "Conversation", 2)
Robot.contenders()
r2d2 = Robot("Optimus", "Fists", 10)
cp30 = Robot("Voltron", "Sword", 10)

Robot.contenders()

##print(r2d2)
##print(cp30)
        
