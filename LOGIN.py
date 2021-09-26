from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("employee_register.db")
c=con.cursor()

obj=Tk()
obj.geometry('500x300')
obj.configure(background='red')

def prevPage():
    obj.destroy()
    import EMPLOYEE

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
a14=StringVar()

def manager():
    
    import sqlite3
    con=sqlite3.connect("employee_register.db")
    c=con.cursor()
    
    global userid
    global password
    global n 
    userid=a4.get()
    
    
    password=a3.get()
    c.execute("select userid from employeedata where userid=?  ",(userid,))
    r=c.fetchall()
    c.execute("select password from employeedata where password=?  ",(password,))
    d=c.fetchall()
    
    a13.set(r)
    n=a13.get()
    k=(n[3:])
    i=(k[:-5])  
    
    a14.set(d)
    m=a14.get()
    m1=(m[3:])
    h=(m1[:-5])
    

    

    if userid==i and password==h:
        messagebox.showinfo('Login', 'your are successfully login')
        def NAME():
            global Name
            updatename=a5.get()
            userid=a4.get()
            
            import sqlite3
            con=sqlite3.connect("employee_register.db")
            c=con.cursor()
            c.execute("update employeedata set Name=? where userid=? ",(updatename,userid))
            c.execute("select * from employeedata where userid=?",(userid,))
            k=c.fetchall()
            print(k)
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
            print(d)
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

        def password():
            global adress
            userid=a4.get()
            
            password=a10.get()
        
            import sqlite3
            con=sqlite3.connect("employee_register.db")
            c=con.cursor()
            c.execute("update employeedata set password=? where userid=?",(password,userid))
            c.execute("select * from employeedata where userid=?",(userid,))
            p=c.fetchall()
            mylist=Listbox(obj,height = 100,width = 120)
            mylist.grid(row=60,column=105)
            for line in range(len(p)):
                mylist.insert(END,p[line])
            con.commit()   
    
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

        b9=Button(obj,text="password",fg="black",bg="white",command=password,font=("Times New Roman",12,'bold'))
        b9.grid(row=51,column=100)
        e9=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a10)
        e9.grid(row=51,column=102)

        b10=Button(obj,text="clear",fg="black",bg="white",command=clear,font=("Times New Roman",12,'bold')).grid(row=52,column=100)
        
    else:
       messagebox.showinfo('Error', 'your data is mis-matched')
    

'''    b9=Button(obj,text="Salary",fg="black",bg="white",command=salary,font=("Times New Roman",12,'bold'))
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
    e11.grid(row=53,column=102)'''

l2=Label(obj,text="User id",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l2.grid(row=0,column=0)    
e3=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a4)
e3.grid(row=0,column=1)


l2=Label(obj,text="password",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l2.grid(row=1,column=0)
e4=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a3)
e4.grid(row=1,column=1)

b3=Button(obj,text="Login",fg="black",bg="white",command=manager,font=("Times New Roman",12,'bold'))
b3.grid(row=2,column=1)

Button(obj,text="EMPLOYEE PORTAL",font=14,bg='pink',command=prevPage).grid(row=3,column=1)
con.commit()
con.close()


obj.mainloop()    
