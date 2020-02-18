from tkinter import *
import SignUp
import TypeSelection

class EnteryPhase:
    labelFont=("couriernew",20)
    gpFont=("couriernew",30)

    def __init__(self):
        self.win=Tk()
        self.win.title("Quiz Game")
        self.win.config(background='white')
        self.win.geometry("{0}x{1}".format(self.win.winfo_screenwidth(),self.win.winfo_screenheight()))
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=0,column=0)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=1,column=1)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=2,column=2)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=3,column=3)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=4,column=4)
        

    def guestPlayer(self):
        gpPlayer=Button(self.win,text="Guest Player",font=self.gpFont,width=15,height=2,bg="white",fg="black")
        gpPlayer.config(relief=RIDGE,command= lambda :self.methodCaller(2))
        gpPlayer.grid(row=3,column=2,columnspan=2)

    def sign_inPlayer(self):
        siPlayer=Button(self.win,text="Sign Up",font=self.gpFont,width=15,height=2,bg="white",fg="black")
        siPlayer.grid(row=3,column=5)
        siPlayer.config(relief=RIDGE,command=lambda:self.methodCaller(1))

    def methodCaller(self,n):
        if(n==1):
            su=SignUp.SignUp()
            su.emailVerification()
            self.win.destroy()
        elif(n==2):
            ts=TypeSelection.TypeSelection(None)
            ts.selection()
            self.win.destroy()

        self.win.mainloop()

ep=EnteryPhase()
ep.guestPlayer()
ep.sign_inPlayer()
