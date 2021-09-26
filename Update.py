from tkinter import *
import sqlite3

con=sqlite3.connect("employee_register.db")
c=con.cursor()

obj=Tk()
obj.geometry('500x300')
obj.configure(background='red')



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

def manager():
    
    import sqlite3
    con=sqlite3.connect("employee_register.db")
    c=con.cursor()
    
    global userid
    userid=a4.get()
    c.execute("select * from employeedata where userid=? ",(userid,))
    con.commit()    
    def NAME():
        global Name
        updatename=a5.get()
        #userid=a4.get()
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set Name=? where userid=? ",(updatename,userid))
        c.execute("select * from employeedata where userid=?",(userid,))
        k=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=55,column=105)
        for line in range(len(k)):
            mylist.insert(END,k[line])
        con.commit()
    def date():
        global date
        userid=a4.get()
        date=a6.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set dob=? where userid=?",(date,userid))
        c.execute("select * from employeedata where userid=?",(userid,))
        d=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()
    def mobile():
        global mobile
        userid=a4.get()
        mobile=a7.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set mobile_no=? where userid=?",(mobile,userid))
        c.execute("select * from employeedata where userid=?",(userid,))
        m=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(m)):
            mylist.insert(END,m[line])
        con.commit()
    def qualification():
        global qualification
        userid=a4.get()
        qualification=a8.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set qualification=? where userid=?",(qualification,userid))
        c.execute("select * from employeedata where userid=?",(userid,))
        n=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(n)):
            mylist.insert(END,n[line])
        con.commit()
    def adress():
        global adress
        userid=a4.get()
        adress=a9.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set adress=? where userid=?",(adress,userid))
        c.execute("select * from employeedata where userid=?",(userid,))
        p=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(p)):
            mylist.insert(END,p[line])
        con.commit()


    def salary ():
        userid=a4.get()
        salary=a10.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set salary=? where userid=?",(salary,userid))
        c.execute("select * from employeedata where userid=?",(userid,))
        q=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(q)):
            mylist.insert(END,q[line])
        con.commit()

    def increment():
        global increment
        userid=a4.get()
        increment=a11.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set increment=? where userid=?",(increment,userid))
        c.execute("select * from employeedata where userid=?",(userid,))
        z=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(z)):
            mylist.insert(END,z[line])
        con.commit()

    def shift():
        global shift
        userid=a4.get()
        shift=a12.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set shift=? where userid=?",(shift,userid))
        c.execute("select * from employeedata where userid=?",(userid,))
        v=c.fetchall()
        
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(v)):
            mylist.insert(END,v[line])
        con.commit()


    
    l2=Label(obj,text="USER ID",fg='black',bg='white',font=("Times New Roman",14,'bold'))
    l2.grid(row=43,column=100)
    e4=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a4)
    e4.grid(row=43,column=102)


    b4=Button(obj,text="UPDATE NAME",fg="black",bg="white",command=NAME,font=("Times New Roman",12,'bold'))
    b4.grid(row=46,column=100)
    e4=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a5)
    e4.grid(row=46,column=102)
    

    b5=Button(obj,text="UPDATE D.O.B.",fg="black",bg="white",command=date,font=("Times New Roman",12,'bold'))
    b5.grid(row=47,column=100)
    e5=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a6)
    e5.grid(row=47,column=102)


    b6=Button(obj,text="UPDATE MOBILE_NUMBER",fg="black",bg="white",command=mobile,font=("Times New Roman",12,'bold'))
    b6.grid(row=48,column=100)
    e6=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a7)
    e6.grid(row=48,column=102)


    b7=Button(obj,text="UPDATE QUALIFICATION",fg="black",bg="white",command=qualification,font=("Times New Roman",12,'bold'))
    b7.grid(row=49,column=100)
    e7=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a8)
    e7.grid(row=49,column=102)

    b8=Button(obj,text="ADRESS",fg="black",bg="white",command=adress,font=("Times New Roman",12,'bold'))
    b8.grid(row=50,column=100)
    e8=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a9)
    e8.grid(row=50,column=102)

    b9=Button(obj,text="Salary",fg="black",bg="white",command=salary,font=("Times New Roman",12,'bold'))
    b9.grid(row=51,column=100)
    e9=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a10)
    e9.grid(row=51,column=102)

    b10=Button(obj,text="Increment",fg="black",bg="white",command=increment,font=("Times New Roman",12,'bold'))
    b10.grid(row=52,column=100)
    e10=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a11)
    e10.grid(row=52,column=102)

    b11=Button(obj,text="shift",fg="black",bg="white",command=shift,font=("Times New Roman",12,'bold'))
    b11.grid(row=53,column=101)
    e11=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a12)
    e11.grid(row=53,column=102)

    
l3=Label(obj,text="User id",fg="black",bg="white",font=("Times New Roman",12,'bold'))
l3.grid(row=0,column=0)
e3=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a4)
e3.grid(row=0,column=1)
b3=Button(obj,text="Click",fg="black",bg="white",command=manager,font=("Times New Roman",12,'bold'))
b3.grid(row=1,column=1)

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
    
b2=Button(obj,text="clear",fg="black",bg="white",command=clear,font=("Times New Roman",12,'bold'))
b2.grid(row=2,column=1)

b2=Button(obj,text="homepage",fg="black",bg="white",command=prevPage,font=("Times New Roman",12,'bold'))
b2.grid(row=3,column=1)    
  
con.commit()
con.close()


obj.mainloop()    
