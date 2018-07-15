from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        #Label
        Label(self, text = "What would you like delivered?").grid(row = 0, column = 0)
        Label(self, text = "Delivery Method: ").grid(row = 2, column = 0)
        Label(self, text = "Addons: ").grid(row = 2, column = 2)
        Label(self, text = "Options").grid(row = 1, column = 1)
        
        #Entry

        deliveryEnt = Entry(self, width = 40)
        deliveryEnt.grid(row = 0, column = 1,columnspan = 2)

        confirmMessage = Text(self, width = 100, height = 4)
        confirmMessage.grid(row = 7,column = 0,columnspan = 3)

        
        self.button_confirm_delivery = Button(self, text='Confirm Delivery', command = self.confirm_delivery)
        self.button_confirm_delivery.grid(row = 6, column = 1)

        self.delivery_method = StringVar()
        self.delivery_method.set(None)
        
        #Radio Button
        #User selects what item(s) they would like delivered
        
        Radiobutton(self, text="Flying Drone($10)",variable = self.delivery_method,value = "flying drone($10)").grid(row = 3,column = 0)

        Radiobutton(self, text="Self Driving Car($20)",variable = self.delivery_method,value = "self driving car($20)").grid(row = 4,column = 0)

        Radiobutton(self, text="Giant Robot($1000)",variable = self.delivery_method,value = "giant robot($1000)").grid(row = 5,column = 0)

        self.express_delivery = BooleanVar()
        self.mostly_not_broken = BooleanVar()
        self.with_a_smile = BooleanVar()

        Checkbutton(self, text="Express Delivery($30)", variable = self.express_delivery).grid(row = 3 ,column = 2 )

        Checkbutton(self, text="Mostly Not Broken($20)", variable = self.mostly_not_broken).grid(row = 4 ,column = 2 )

        Checkbutton(self, text="With a Smile($1)", variable = self.with_a_smile).grid(row = 5,column = 2)


    def confirm_delivery(self):
    #The error says I'm not .get() the entry but I am
    #I was in office hours working on this along with UI
    #The UI said that it should work however we ran out of time
    #So the error was not fixed
       fee = 0
       message = "You have selected a"  
       message += self.deliveryEnt.get() + "delivered by" 
       message += self.delivery_method.get() + " "
       

       if self.express_delivery.get():
           message += "express delivery."
           fee += 30

       if self.most_not_broken.get():
                message += "mostly not broken."
                fee += 20

       elif self.with_a_smile.get():
                message += "with a smile"
                fee += 1

       elif self.most_not_broken.get():
            message += "express delivery."
            fee += 30

            if self.with_a_smile.get():
                message += "with a smile"
                fee += 1

            elif self.express_delivery.get():
                message += "express delivery."
                fee += 30

       elif self.with_a_smile.get():
            message += "with a smile"
            fee += 1

       elif self.express_delivery.get() and self.most_not_broken and self.with_a_smile == False:
            message += "with no options."
            message += "Your total delivery fee comes to: " + str(fee) + "."
            self.confirmMessage.delete(0.0, END)
            self.confirmMessage.insert(0.0, message)
           
       
           
           
           



# main
root = Tk()
root.title("Robot Delivery System")
root.geometry("750x350")

app = Application(root)
root.mainloop()
