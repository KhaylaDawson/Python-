#9.20
#9.21
#9.22
import random
from tkinter import *
from tkinter.messagebox import showinfo

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):
        self.lbl = Label(self, text="Enter your guess: ")
        self.lbl.grid()
        self.bttn1 = Button(self, text = "Enter", command = self.random_guess)
        self.bttn1.grid(row = 2, column = 1, columnspan = 2)

o       self.numEnt = Entry(self)
        self.numEnt.grid(row = 0, column = 1)
        self.randnum = random.randrange(0, 9)
        self.bttn1.bind("<KeyPress>", self.click)
        self.bttn1.focus_set()

    def random_guess(self):
        #Generates random number when user inputs a number
        #Secret number between 0 and 9 is chosen
        #User enters numbers until correct guess is shown
        #Tracing to help put out input
        if self.randnum == int(self.numEnt.get()):
            showinfo(message = "Correct guess! Let's do this again")
            self.numEnt.delete(0, END)
            self.randnum = random.randrange(0, 9)
            #If the entry is a blank space run the guess again
            self.random_guess()
            

    def click(self, event):
        #Allows the user to click the ENTER button off the keyboard
        #Instead of using the mouse to click the ENTER button
        if event.keysym == "Return":
            self.random_guess()




# main
root = Tk()
root.title("tk")
root.geometry("300x100")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
