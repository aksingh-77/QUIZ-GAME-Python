import sqlite3
from tkinter import *
import random
import OTPConfirm

class SQLMode:
    _labelFont=("couriernew",20)
    _gpFont=("couriernew",30)
    _ans=list()
    
    def __init__(self):
        self._sports=list()
        self._win=Tk()
        self._win.config(background='white')
        self._frame=Frame(self._win,width=self._win.winfo_screenwidth(),height=200)
        self._frame.grid(row=1,column=0)
        
        self._win.title("Game Mode")
        self._win.geometry("{0}x{1}".format(self._win.winfo_screenwidth(),self._win.winfo_screenheight()))
        Label(self._win,text="  ",width=10,height=3,bg='white').grid(row=0,column=0)

    def _sqlConnection(self,mode):
        try:
            self.__conn=sqlite3.connect('questionBank.db')
            self.__cur=self.__conn.cursor()
        except (sqlite3.OperationalError)as  e:
            print("Error",e )
        else:
            #-------------------------- Sports ------------------------------
            if(mode==1):
                try:
                    sportsList=random.sample(range(24),10)
                    for num in sportsList:
                        self.__cur.execute('''select question,optiona,optionb,optionc,optiond,answers
from sport
where id=? ''',(num,))
                        temp=self.__cur.fetchone()
                        self._sports.append(temp)
                except (Exception)as e:
                    print(e)
                    #-------------------------- Python ------------------------------
            elif(mode==2):
                try:
                    sportsList=random.sample(range(21),10)
                    for num in sportsList:
                        self.__cur.execute('''select question,optiona,optionb,optionc,optiond,answers
from python
where id=? ''',(num,))
                        temp=self.__cur.fetchone()
                        self._sports.append(temp)
                except (Exception)as e:
                    print(e)

                    #-------------------------- Maths ------------------------------
            elif(mode==3):
                try:
                    sportsList=random.sample(range(20),10)
                    for num in sportsList:
                        self.__cur.execute('''select question,optiona,optionb,optionc,optiond,answers
from maths
where id=? ''',(num,))
                        temp=self.__cur.fetchone()
                        self._sports.append(temp)
                except (Exception)as e:
                    print(e)
        finally:
            self.__cur.close()
            self.__conn.close()

#========================================== UI ----------------------------------------
class GameUI(SQLMode):
    __questions=list()
    __answers=list()
    __options=list()
    __counter=0
    __optionCounter=0

    def __init__(self,n,email):
        super().__init__()
        self.__value=StringVar()
        self.__win=self._win
        self._sqlConnection(n)
        self.__data=self._sports
        self.wd=self._win.winfo_screenwidth()
        self.__ans=self._ans
        self.email=email

        for data in self.__data:
            self.__questions.append(data[0])
            self.__options.append((data[1],data[2],data[3],data[4]))
            self.__answers.append(data[5])

    def deleteButton(self):
        x=self.__value.get()
        self.__ans.append(x)
        if (self.t1):
            self.canvas.delete(self.t1)
            self.canvas.delete(self.t2)
            self.canvas.delete(self.t3)
            self.canvas.delete(self.t4)
            self.canvas.delete(self.t5)
            self.t1 = None
            self.t2 = None
            self.t3 = None
            self.t4=None
            self.t5=None
            self.__counter+=1
            self.__optionCounter+=1
            self.ll1.destroy()
            self.ll2.destroy()
            self.ll3.destroy()
            self.ll4.destroy()
            GameUI.finalUI(self)

    def finalUI(self):
        if(self.__counter==10):
            self.__win.destroy()
            score=0
            correct=dict()

            for a in range(0,len(self.__answers)):
                self.__answers[a]=self.__answers[a].replace('=','')

            for x in range(0,len(self.__answers)):
                if(self.__answers[x]==self.__ans[x]):
                    score+=1
                    correct[x+1]='Correct'
                else:
                    correct[x+1]='Wrong'
            if(self.email):
                OTPConfirm.confirmationMail(self.email,score,correct)
            
            
            win=Tk()
            win.title("Game Mode")
            win.config(background='white')
            win.geometry("{0}x{1}".format(win.winfo_screenwidth(),win.winfo_screenheight()))
            Label(win,text="",width=10,height=3,font=self._labelFont,bg='white').grid(row=0,column=0)
            Label(win,text="",width=10,height=3,font=self._labelFont,bg='white').grid(row=1,column=1)
            Label(win,text="",width=10,height=3,font=self._labelFont,bg='white').grid(row=2,column=2)
            Label(win,text="",width=10,height=3,font=self._labelFont,bg='white').grid(row=3,column=3)
            Label(win,text="Score",width=10,height=3,font=("couriernew",30),bg='white').grid(row=3,column=3)
            Label(win,text=score,width=10,height=3,font=("couriernew",40),bg='white').grid(row=4,column=3)

            nextButton=Button(win,text="Exit",font=self._gpFont,width=10,height=1,relief=RIDGE,bg='white')
            nextButton.grid(row=5,column=3,sticky=N)
            nextButton.config(command=lambda:win.destroy())
                        
        else:
            #self.__value=StringVar()
            txt=self.__questions[self.__counter].split(" ")
            
            #del txt[0]
            #--------------------------------------  << Canvas >> -------------------------------------------
            if(self.__counter==0):
                self.canvas=Canvas(self._frame,bg='#FFFFFF',width=self.wd,height=200,scrollregion=(0,0,self.wd,400))

                hbar=Scrollbar(self._frame,orient=HORIZONTAL)
                hbar.pack(side=BOTTOM,fill=X)
                hbar.config(command=self.canvas.xview)
                
                vbar=Scrollbar(self._frame,orient=VERTICAL)
                vbar.pack(side=RIGHT,fill=Y)
                vbar.config(command=self.canvas.yview)
                
                self.canvas.config(width=self.wd-500,height=100)
                self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
                self.canvas.pack(side=LEFT,expand=True,fill=BOTH)
                
            self.t1=self.canvas.create_text(400,30,fill="darkblue",font="Times 20 italic bold",text=txt[:10])
            self.t2=self.canvas.create_text(400,50,fill="darkblue",font="Times 20 italic bold",text=txt[10:20])
            self.t3=self.canvas.create_text(400,70,fill="darkblue",font="Times 20 italic bold",text=txt[20:30])
            self.t4=self.canvas.create_text(400,90,fill="darkblue",font="Times 20 italic bold",text=txt[30:40])
            self.t5=self.canvas.create_text(400,110,fill="darkblue",font="Times 20 italic bold",text=txt[30:40])

            #--------------------------------------   <Options> ----------------------------------------------------
            option1=Radiobutton(self.__win,text="",font=self._gpFont,variable=self.__value,value='a',indicatoron =1,width=2,bg='white')
            option1.grid(row=2,sticky=W)
            self.ll1=Label(self.__win,text=self.__options[self.__optionCounter][0],font=self._gpFont,bg='white')
            self.ll1.grid(row=2,sticky=N)
            
            option2=Radiobutton(self.__win,text="",font=self._gpFont,variable=self.__value,indicatoron = 1,value='b',width=2,bg='white')
            option2.grid(row=3,sticky=W)
            self.ll2=Label(self.__win,text=self.__options[self.__optionCounter][1],font=self._gpFont,bg='white')
            self.ll2.grid(row=3,sticky=N)
            
            option3=Radiobutton(self.__win,text="",font=self._gpFont,variable=self.__value,indicatoron = 1,value='c',width=2,bg='white')
            option3.grid(row=4,sticky=W)
            self.ll3=Label(self.__win,text=self.__options[self.__optionCounter][2],font=self._gpFont,background='white',bg='white')
            self.ll3.grid(row=4,sticky=N)
            
            option4=Radiobutton(self.__win,text="",font=self._gpFont,variable=self.__value,indicatoron = 1,value='d',width=2,bg='white')
            option4.grid(row=5,sticky=W)
            self.ll4=Label(self.__win,text=self.__options[self.__optionCounter][3],font=self._gpFont,bg='white')
            self.ll4.grid(row=5,sticky=N)
            
            nextButton=Button(self.__win,text="Next",font=self._gpFont,relief=RIDGE,width=10,height=1)
            nextButton.grid(row=6,column=0,sticky=N)
            nextButton.config(command=lambda:GameUI.deleteButton(self),bg='white')
        
#gg=GameUI(2,"hello")
#gg.finalUI()
