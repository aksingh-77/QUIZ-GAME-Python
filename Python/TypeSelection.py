from tkinter import *
from GameMode import *

class TypeSelection:
    labelFont=("couriernew",20)
    buttonFont=("couriernew",30)

    def __init__(self,email):
        self.win=Tk()
        self.win.title("Mode Selection")
        self.win.config(background='white')
        self.win.geometry("{0}x{1}".format(self.win.winfo_screenwidth(),self.win.winfo_screenheight()))
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,bg='white').grid(row=0,column=0)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,bg='white').grid(row=1,column=1)
        Label(self.win,text="   ",font=self.labelFont,width=10,height=3,bg='white').grid(row=2,column=2)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,bg='white').grid(row=3,column=4)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,bg='white').grid(row=4,column=3)
        self.email=email
        TypeSelection.selection(self)

    def modeSelection(self,n):
        if(n==1):
            self.win.destroy()
            gg=GameUI(1,self.email)
            gg.finalUI()
        elif(n==2):
            self.win.destroy()
            gg=GameUI(2,self.email)
            gg.finalUI()
        elif(n==3):
            self.win.destroy()
            gg=GameUI(3,self.email)
            gg.finalUI()

    def selection(self):
        #----------------------------------- Sports Time -------------------------------------------------
        quiz=Button(self.win,text=" Sports",font=self.buttonFont,width=12,height=2,bg="white",fg="black")
        quiz.grid(row=3,column=2)
        quiz.config(relief=RIDGE,command=lambda:TypeSelection.modeSelection(self,1))

        #----------------------------------- Maths Time -------------------------------------------------
        maths=Button(self.win,text=" Maths ",font=self.buttonFont,width=12,height=2,bg="white",fg="black")
        maths.grid(row=3,column=4)
        maths.config(relief=RIDGE,command=lambda:TypeSelection.modeSelection(self,3))
        

        #----------------------------------- Python Time -------------------------------------------------
        python=Button(self.win,text="Python Snippets",font=self.buttonFont,width=15,height=2,bg="white",fg="black")
        python.grid(row=5,column=3)
        python.config(relief=RIDGE,command=lambda:TypeSelection.modeSelection(self,2))

#ts=TypeSelection()
#ts.selection()
