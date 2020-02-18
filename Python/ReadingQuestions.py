from re import *
import sqlite3

#--------------------------------------------  SQL ----------------------------------------------------
def SQLConnection(questions,options,answers):
    sportTable="""create table sport
(
id int,
question text(200),
optiona text(5),
optionb text(5),
optionc text(5),
optiond text(5),
answers text(2))"""

    pythonTable='''create table python(
id int,
question text(200),
optiona text(5),
optionb text(5),
optionc text(5),
optiond text(5),
answers text(2))'''

    mathTable='''create table maths(
id int,
question text(200),
optiona text(5),
optionb text(5),
optionc text(5),
optiond text(5),
answers text(2))'''
    
    try:
        conn=sqlite3.connect("questionBank.db")
        cur=conn.cursor()
        #cur.execute(sportTable)
        #cur.execute(mathTable)
        #cur.execute(pythonTable)

        '''for x in range(0,len(questions)-1):
            cur.execute('insert into python(id,question,optiona,optionb,optionc,optiond,answers) values(?,?,?,?,?,?,?)'
                        ,(x,questions[x],options[x][0],options[x][1],options[x][2],options[x][3],answers[x]))
        conn.commit()'''


        values=cur.execute("select * from python")
        for x in values:
            print(x[1])
        
    except (sqlite3.OperationalError)as  e:
        print("Error",e )
    else:
        
        print("Table Created")
    finally:
        cur.close()
        conn.close()

#--------------------------------------------  SPORTS ----------------------------------------------------    
'''with open(r'Question/sports.txt','r')as file:
    #print(file.readlines())
    data=file.read()
    option=list()
    
    temp=findall(r'^\d{1,2}.+\?$',data,M)
    temp1=findall(r'^[a-d]\).+',data,M)
    temp2=findall(r'=[a-z]$',data,M)

    answers=list(filter(None,temp2))
    
    options=[ o if len(temp1)>0 else quit() for o in temp1]
    questions=[q if len(temp)>0 else quit() for q in temp]

    for x in range(1,len(options)+1):
        if(x%4==0):
            option.append((options[x-4],options[x-3],options[x-2],options[x-1]))

   # SQLConnection(questions,option,answers)
        
#-------------------------------------------- MATHS  ----------------------------------------------------
with open(r'Question/pythonn.txt',encoding = "ISO-8859-1")as file:
    #print(file.readlines())
    data=file.read()
    option=list()
    
    temp=findall(r'^\d{1,2}.+\?$',data,M)
    temp1=findall(r'^\([a-d]\).+',data,M)
    temp2=findall(r'=[a-z]$',data,M)

    answers=list(filter(None,temp2))
    options=[ o if len(temp1)>0 else quit() for o in temp1]
    questions=[q if len(temp)>0 else quit() for q in temp]

    for x in options:
        option.append(tuple(filter(None,x.split(' '))))
        

    for x in range(1,len(options)+1):
        if(x%4==0):
            option.append((options[x-4],options[x-3],options[x-2],options[x-1]))
    SQLConnection(questions,option,answers)

'''
#--------------------------------------------  PYTHON ----------------------------------------------------
def PythonQuestion():
    with open(r'Question/py.txt', encoding="utf-8")as file:
        data=file.read()
        temp=findall(r'^\d{1,2}.+\?$',data,M)
        questions=[q if len(temp)>0 else quit() for q in temp]

    with open(r'Question/py.txt', encoding="utf-8")as file:
        data=file.read()

        temp1=findall(r'^[A-D]\).+',data,M)
        temp2=findall(r'=[a-z]$',data,M)

        answers=list(filter(None,temp2))
        options=[ o if len(temp1)>0 else quit() for o in temp1]

        answers.insert(14,'b')
        answers.insert(16,'b')
        answers.insert(17,'b')
        answers.insert(18,'d')
        answers.insert(19,'d')

        option=list()
        for x in range(1,len(options)+1):
            if(x%4==0):
                option.append((options[x-4],options[x-3],options[x-2],options[x-1]))
        SQLConnection(questions,option,answers)
        
PythonQuestion()
