from tkinter import *



obj=Tk()
obj.geometry('500x300')
obj.configure(background='pink')

a4=StringVar()

def delete():
    
    import sqlite3
    con=sqlite3.connect("employee_register.db")
    c=con.cursor()
    
    global userid
    userid=a4.get()
    c.execute("Delete from employeedata where userid=? ",(userid,))
    c.execute("select * from employeedata ")
    d=c.fetchall()
    mylist=Listbox(obj,height = 100,width = 120)
    mylist.grid(row=60,column=105)
    for line in range(len(d)):
        mylist.insert(END,d[line])
    con.commit()

l2=Label(obj,text="Enter user id",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l2.grid(row=1,column=0)
e4=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a4)
e4.grid(row=1,column=1)
    
b4=Button(obj,text="Delete Data",fg="black",bg="white",command=delete,font=("Times New Roman",12,'bold'))
b4.grid(row=2,column=1)


def prevPage():
    obj.destroy()
    import home_page
b2=Button(obj,text="homepage",fg="black",bg="white",command=prevPage,font=("Times New Roman",12,'bold'))
b2.grid(row=3,column=1)
