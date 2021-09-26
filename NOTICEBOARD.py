from tkinter import *

top=Tk()
top.geometry('800x800')
top.title('NOTICEBOARD')
top.configure(background='#E6E6FA')

import sqlite3
con=sqlite3.connect("employee_register.db")
c=con.cursor()

name=StringVar()
namedata="nothing"
department="Choose"
def search():
    global namedata
    n=name.get()
    n=n.lower()
    namedata=n
    if namedata!="nothing" and department!="Choose":
        c.execute("select userid,Name,department,shift from employeedata where Name=? and department=?",(namedata,department))
    else:
        c.execute("select userid,Name,department,shift from employeedata where name=?",(namedata,))
    d=c.fetchall()
    sc= Scrollbar(top)
    sc.grid(row=6,column=6)
    mylist = Listbox(top, yscrollcommand = sc.set,width=100 )
    for line in range(len(d)):
        mylist.insert(END,d[line])
    mylist.grid(row=6,column=5)
    sc.config( command = mylist.yview )
    con.commit()

l1=Label(top,text="Enter employee name:",fg='#FF69B4',bg='#FFF68F',font=("Times New Roman",14,'bold'))
l1.grid(row=0,column=1)
e1=Entry(top,justify="left",bg="white",bd=5,insertwidth=5,textvariable=name)
e1.grid(row=0,column=3)

b1=Button(top,text="search",fg="black",bg="#00FF00",font=("Times New Roman",12,'bold'),command=search)
b1.grid(row=5,column=3)

c.execute("select department from employeedata")
dd=c.fetchall()
dp=list(set(list(map(lambda x:x[0],dd))))
var=StringVar(top)
var.set("department")

def selectedvalue(x):
    global department
    department=x
    if namedata!="nothing" and department!="Choose":
        c.execute("select userid,Name,department,shift from employeedata where name=? and department=?",(namedata,department))
    else:
        c.execute("select userid,Name,department,shift from employeedata where department=?",(department,))
    d=c.fetchall()
    sc= Scrollbar(top)
    sc.grid(row=6,column=6)
    mylist = Listbox(top, yscrollcommand = sc.set,width=100 )
    for line in range(len(d)):
        mylist.insert(END,d[line])
    mylist.grid(row=6,column=5)
    sc.config( command = mylist.yview )
    
    con.commit()

dp=OptionMenu(top,var,*dp,command=selectedvalue)
dp.grid(row=5,column=5)


c.execute("select userid,Name,department,shift from employeedata")
d=c.fetchall()
sc= Scrollbar(top)
sc.grid(row=6,column=6)
mylist = Listbox(top, yscrollcommand = sc.set,width=100)
for line in range(len(d)):
    mylist.insert(END,d[line])
mylist.grid(row=6,column=5)
sc.config( command = mylist.yview )

    
con.commit()

def back():
    top.destroy()
    import EMPLOYEE
    

b1=Button(top,text="previous",fg="#00FF00",bg="#EE2C2C",font=("Times New Roman",12,'bold'),command=back)
b1.grid(row=9,column=5)

top.mainloop()


