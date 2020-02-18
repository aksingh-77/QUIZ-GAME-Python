from tkinter import *
from re import *
import random
import OTPConfirm
import TypeSelection

class SignUp:
    labelFont=("couriernew",17)
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
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=4,column=3)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=5,column=3)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=6,column=3)
        Label(self.win,text="  ",font=self.labelFont,width=10,height=3,background='white').grid(row=7,column=3)

    def emailVerification(self):
        #---------------------------- Email Entry ------------------------------------
        self.email=Entry(self.win,width=22,font=self.gpFont)
        self.email.insert(0,"Email ID")
        self.email.grid(row=2,column=4,columnspan=3,rowspan=2)

        #---------------------------------Submit Button -------------------------
        submit=Button(self.win,text="Submit",font=self.gpFont,width=10,height=2,bg="white",fg="black")
        submit.grid(row=7,column=5,rowspan=2)
        submit.config(command=lambda:self.otpMethod())

    def otpMethod(self):
        mail=self.email.get().strip()
        self.otp=random.randint(1000,9999)

        # ================================ OTP Time ==============================================
        OTPConfirm.confirmationMail(mail,1,self.otp)

        Label(self.win,text="OTP",font=self.labelFont).grid(row=4,column=1)
        self.newOtp=Entry(self.win,show='*',font=self.labelFont)
        self.newOtp.grid(row=4,column=4,columnspan=2)
        print(self.otp)

        submit=Button(self.win,text="OTP Submit",font=self.gpFont,width=10,height=2,bg="Black",fg="#C0C0C0")
        submit.grid(row=7,column=5,rowspan=2)
        submit.config(command=lambda:self.passwordField())

    def passwordField(self):
        temp=self.newOtp.get().strip()
        temp=int(temp)

        if(self.otp==temp):
            Label(self.win,text="Registration Done",font=self.gpFont).grid(row=1,column=3,columnspan=3)

            submit=Button(self.win,text="  Menu  ",font=self.gpFont,width=10,height=2,bg="Black",fg="#C0C0C0")
            submit.grid(row=7,column=5,rowspan=2)
            submit.config(command=lambda:self.finalRegistration())

    def finalRegistration(self):
        mail=self.email.get().strip()
        ts=TypeSelection.TypeSelection(mail)
        ts.selection()
        self.win.destroy()
    
            

#su=SignUp()
#su.emailVerification()
