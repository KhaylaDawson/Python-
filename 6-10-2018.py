##from tkinter import *
##import random
##
##class Application(Frame):
##
##    def __init__(self, master):
##        Frame.__init__(self, master)
##        self.grid()
##        self.create_widgets()
##
##    def create_widgets(self):
##        self.title = Label(self, text="Roman Numeral Canvas")
##        self.title.grid(row=0, column=0, columnspan = 4)
##
##        self.canvas = Canvas(self, height=310, width=500)
##        self.canvas.grid(row = 1, column = 0, columnspan = 2, rowspan = 3)
##
##        self.wid_lbl = Label(self, text="Numbers:")
##        self.wid_lbl.grid(row = 1, column = 2)
##
##        self.numberEntry = Entry(self, width=20)
##        self.numberEntry.grid(row = 1, column = 3)
##
##        self.rdj = BooleanVar()
##        self.rdj.set(False)
##        Checkbutton(self,text="Numbers",variable=self.rdj,command=self.updatetext).grid(row=1,column=4)
##
##        self.color_lbl = Label(self, text="Line Width:")
##        self.color_lbl.grid(row = 2, column = 2)
##
##        self.lineWidth = StringVar()
##        self.lineWidth.set('1')
##        Radiobutton(self,text='1',variable=self.lineWidth,value='1',command=self.updatetext).grid(row=2,column=3)
##        Radiobutton(self,text='3',variable=self.lineWidth,value='3',command=self.updatetext).grid(row=2,column=4)
##        Radiobutton(self,text='5',variable=self.lineWidth,value='5',command=self.updatetext).grid(row=2,column=5)
##
##        self.length_lbl = Label(self, text="Line Color:")
##        self.length_lbl.grid(row = 3, column = 2)
##
##        self.color = StringVar()
##        self.color.set('Black')
##        Radiobutton(self,text='Black',variable=self.color,value='Black',command=self.updatetext).grid(row=3,column=3)
##        Radiobutton(self,text='Red',variable=self.color,value='Red',command=self.updatetext).grid(row=3,column=4)
##        Radiobutton(self,text='Blue',variable=self.color,value='Blue',command=self.updatetext).grid(row=3,column=5)
##
##        self.roman = PhotoImage(file='roman.gif')
##        self.romanBttn = Button(self,image=self.roman,command=self.updateRoman)
##        self.romanBttn.grid(row=4,rowspan=3,column=3,sticky=W)
##
##        self.random = PhotoImage(file='random.gif')
##        self.randomBttn = Button(self,image=self.random,command=self.randomExtraCredit)
##        self.randomBttn.grid(row=4,rowspan=3,column=4,sticky=W)
##
##        self.x, self.y = 20, 20
##
##    def updatetext(self):
##        pass
##
##
##    def convertNumToString(self, mainString):
##        finalString = ""
##        mainInt = int(mainString)
##        while True:
##            print(mainInt)
##            if mainInt - 1000 >= 0:
##                mainInt = mainInt - 1000
##                finalString+="m"
##            elif mainInt - 500 >= 0:
##                mainInt = mainInt - 500
##                finalString+="d"
##            elif mainInt - 100 >= 0:
##                mainInt = mainInt - 100
##                finalString+="c"
##            elif mainInt - 50 >= 0:
##                mainInt = mainInt - 50
##                finalString+="l"
##            elif mainInt - 10 >= 0:
##                mainInt = mainInt - 10
##                finalString+="x"
##            elif mainInt - 5 >= 0:
##                mainInt = mainInt - 5
##                finalString+="v"
##            elif mainInt - 1 >= 0:
##                mainInt = mainInt - 1
##                finalString+="i"
##            else:
##                break
##        return finalString
##
##
##
##    def randomExtraCredit(self):
##
##        # Check if the numbers checkbox is done
##        if self.rdj.get():
##            totalString = self.convertNumToString(self.numberEntry.get())
##        else:
##            totalString = self.numberEntry.get()
##
##        # Random options that are available
##        widthOptions = [1,2,3,4,5]
##        colorOptions = ["black","red","blue","green"]
##
##        for letter in totalString:
##            correctValFound = True
##            lineWidth = random.choice(widthOptions)
##            color = random.choice(colorOptions)
##            if letter.lower() == "m":
##                self.draw_M(lineWidth, color)
##            elif letter.lower() == "d":
##                self.draw_D(lineWidth, color)
##            elif letter.lower() == "c":
##                self.draw_C(lineWidth, color)
##            elif letter.lower() == "l":
##                self.draw_L(lineWidth, color)
##            elif letter.lower() == "x":
##                self.draw_X(lineWidth, color)
##            elif letter.lower() == "v":
##                self.draw_V(lineWidth, color)
##            elif letter.lower() == "i":
##                self.draw_I(lineWidth, color)
##            else:
##                # Make sure a letter was shown before tab
##                correctValFound = False
##
##            # Tab down if there are too many letters on screen
##            if self.x > 450 and correctValFound:
##                self.x = 20
##                self.y += 50
##
##
##    def updateRoman(self):
##        # Check if the numbers checkbox is done
##        if self.rdj.get():
##            totalString = self.convertNumToString(self.numberEntry.get())
##        else:
##            totalString = self.numberEntry.get()
##
##        lineWidth = int(self.lineWidth.get())
##        color = self.color.get()
##
##        for letter in totalString:
##            correctValFound = True
##            if letter.lower() == "m":
##                self.draw_M(lineWidth, color)
##            elif letter.lower() == "d":
##                self.draw_D(lineWidth, color)
##            elif letter.lower() == "c":
##                self.draw_C(lineWidth, color)
##            elif letter.lower() == "l":
##                self.draw_L(lineWidth, color)
##            elif letter.lower() == "x":
##                self.draw_X(lineWidth, color)
##            elif letter.lower() == "v":
##                self.draw_V(lineWidth, color)
##            elif letter.lower() == "i":
##                self.draw_I(lineWidth, color)
##            else:
##                # Make sure a letter was shown before tab
##                correctValFound = False
##
##            # Tab down if there are too many letters on screen
##            if self.x > 450 and correctValFound:
##                self.x = 20
##                self.y += 50
##
##
##    def draw_M(self, lineWidth, color):
##        self.canvas.create_line(self.x, self.y, self.x+5, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+15, self.y, self.x+20, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+3, self.y, self.x+10, self.y+10, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+10, self.y+10, self.x+17, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+3, self.y, self.x+3, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+17, self.y, self.x+17, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y+40, self.x+5, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+15, self.y+40, self.x+20, self.y+40, width=lineWidth, fill=color)
##        self.x += 20 + 10
##
##    def draw_D(self, lineWidth, color):
##        self.canvas.create_line(self.x, self.y, self.x, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y, self.x+10, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y+40, self.x+10, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+10, self.y, self.x+20, self.y+10, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+10, self.y + 40, self.x+20, self.y+30, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+20, self.y + 10, self.x+20, self.y+30, width=lineWidth, fill=color)
##        self.x += 20 + 10
##
##    def draw_C(self, lineWidth, color):
##        self.canvas.create_line(self.x, self.y+10, self.x, self.y+30, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y+10, self.x+10, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y+30, self.x+10, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+10, self.y, self.x+20, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+10, self.y+40, self.x+20, self.y+40, width=lineWidth, fill=color)
##        self.x += 20 + 10
##
##    def draw_L(self, lineWidth, color):
##        self.canvas.create_line(self.x, self.y, self.x+5, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+3, self.y, self.x+3, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=lineWidth, fill=color)
##        self.x += 20 + 10
##
##    def draw_X(self, lineWidth, color):
##        self.canvas.create_line(self.x, self.y, self.x+20, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+5, self.y, self.x+15, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+15, self.y, self.x+5, self.y+40, width=lineWidth, fill=color)
##        self.x += 20 + 10
##
##    def draw_V(self, lineWidth, color):
##        self.canvas.create_line(self.x, self.y, self.x+20, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+5, self.y, self.x+10, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+10, self.y+40, self.x+15, self.y, width=lineWidth, fill=color)
##        self.x += 20 + 10
##
##    def draw_I(self, lineWidth, color):
##        self.canvas.create_line(self.x, self.y, self.x+20, self.y, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=lineWidth, fill=color)
##        self.canvas.create_line(self.x+10, self.y, self.x+10, self.y+40, width=lineWidth, fill=color)
##        self.x += 20 + 10
##
##
### main
##root = Tk()
##root.title("Roman Numerals")
##root.geometry("900x350")
##
##app = Application(root)
