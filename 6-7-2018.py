from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Enter student information")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 3, sticky = S)

        self.studname_lbl = Label(self, text = "Student Name: ")
        self.studname_lbl.grid(row = 1, column = 0, sticky = W)

        self.gpa_lbl = Label(self, text = "GPA: ")
        self.gpa_lbl.grid(row = 2, column = 0, sticky = W)

        self.essay_lbl = Label(self, text = "Essay: ")
        self.essay_lbl.grid(row = 3, column = 0, sticky = W)

        self.save_bttn = Button(self, text = "Save")
        self.clear_bttn = Button(self, text = "Clear")

        self.student_name = Entry(self, width=40)
        self.student_name.grid(row=1, column=1, columnspan=2, sticky=W)

        self.student_gpa = Entry(self, width=40)
        self.student_gpa.grid(row=2, column=1, columnspan=2, sticky=W)

        self.essay = Text(self, width = 50, height = 10, wrap = WORD)
        self.essay.grid(row = 4, column = 0, columnspan = 3, sticky = W)


root = Tk()
root.title("College Application")
root.geometry("410x280")
#root.resizeable(width = FALSE, height = FALSE)
app = Application(root)
root.mainloop()                                 
