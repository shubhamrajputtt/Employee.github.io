print("wlcome")

from tkinter import *
import sqlite3

obj=Tk()
obj.geometry('500x300')
obj.configure(background='red')
def SIGNUP():
    obj.destroy()
    import managerlogin


a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()
a6=StringVar()
a7=StringVar()
a8=StringVar()
a9=StringVar()
a10=StringVar()
a11=StringVar()
a12=StringVar()
a13=StringVar()
con=sqlite3.connect("employee_register.db")
c=con.cursor()
#c.execute("create table managerdata (Name text,userid text,password text,shift text,designation text,department text,salary int, increment int,dob string,adress text,mobile_no int,qualification string)")
con.commit()

l1=Label(obj,text="Name:",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l1.grid(row=0,column=0)
e1=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a1)
e1.grid(row=0,column=5)


l2=Label(obj,text="USER ID",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l2.grid(row=3,column=0)
e2=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a2)
e2.grid(row=3,column=5)

'''l3=Label(obj,text="PASSWORD",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l3.grid(row=6,column=0)
e3=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a3)
e3.grid(row=6,column=5)'''

l4=Label(obj,text="SHIFT",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l4.grid(row=7,column=0)
e4=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a4)
e4.grid(row=7,column=5)

l5=Label(obj,text="DESIGNATION",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l5.grid(row=8,column=0)
e5=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a5)
e5.grid(row=8,column=5)

l6=Label(obj,text="DEPARTMENT",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l6.grid(row=9,column=0)
e6=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a6)
e6.grid(row=9,column=5)

l7=Label(obj,text="SALARY",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l7.grid(row=10,column=0)
e7=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a7)
e7.grid(row=10,column=5)

l8=Label(obj,text="INCREMENT",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l8.grid(row=11,column=0)
e8=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a8)
e8.grid(row=11,column=5)

l9=Label(obj,text="DATE OF BIRTH",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l9.grid(row=12,column=0)
e9=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a9)
e9.grid(row=12,column=5)

l10=Label(obj,text="adress",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l10.grid(row=13,column=0)
e10=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a10)
e10.grid(row=13,column=5)

l11=Label(obj,text="MOBILE_no.",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l11.grid(row=14,column=0)
e11=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a11)
e11.grid(row=14,column=5)

l12=Label(obj,text="QUALIFICATION",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l12.grid(row=15,column=0)
e12=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a12)
e12.grid(row=15,column=5)

def clear():
    a1.set("")
    a2.set("")
    a3.set("")
    a4.set("")
    a5.set("")
    a6.set("")
    a7.set("")
    a8.set("")
    a9.set("")
    a10.set("")
    a11.set("")
    a12.set("")
def prevPage():
    obj.destroy()
    import home_page

def insert():
    Name=a1.get()
    userid=a2.get()
    password=a3.get()
    shift=a4.get()
    designation=a5.get()
    department=a6.get()
    salary=a7.get()
    increment=a8.get()
    birth_date=a9.get()
    adress=a10.get()
    mobile_no=a11.get()
    qualification=a12.get()
    
    con=sqlite3.connect("employee_register.db")
    c=con.cursor()
    c.execute("INSERT INTO employeedata VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(Name,userid,password,shift,designation,department,salary,increment,birth_date,adress,mobile_no,qualification))
    c.execute("select * from employeedata where userid=?",(userid,))
    d=c.fetchall()
    mylist=Listbox(obj,height = 100,width = 120)
    mylist.grid(row=60,column=105)
    for line in range(len(d)):
        mylist.insert(END,d[line])
    con.commit()
    
    

b2=Button(obj,text="ADD",fg="black",bg="white",command=insert,font=("Times New Roman",12,'bold'))
b2.grid(row=20,column=5)
b3=Button(obj,text="LOG IN",fg="black",bg="white",command=SIGNUP,font=("Times New Roman",12,'bold'))
b3.grid(row=30,column=5)

b2=Button(obj,text="clear",fg="black",bg="white",command=clear,font=("Times New Roman",12,'bold'))
b2.grid(row=31,column=5)

b2=Button(obj,text="homepage",fg="black",bg="white",command=prevPage,font=("Times New Roman",12,'bold'))
b2.grid(row=32,column=5)

obj.mainloop()

print("thnks")
