from tkinter import *
from tkinter import messagebox
obj=Tk()
obj.geometry('1000x800')
obj.title('LOGIN PORTAL')


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
a15=StringVar()
def enter():
    import sqlite3
    con=sqlite3.connect("employee_register.db")
    c=con.cursor()
    global userid
    global password
    global department
    department=a3.get()
    userid=a1.get()
    password=a2.get()
    
    c.execute("select userid from managerdata where userid=? ",(userid,))
    w=c.fetchall()
    
    c.execute("select password from managerdata where password=? ",(password,))
    v=c.fetchall()
   
    c.execute("select department from managerdata where department=? ",(department,))
    n=c.fetchall()

    a13.set(w)
    x=a13.get()
    k=(x[3:])
    i=(k[:-5])
    

    a14.set(v)
    y=a14.get()
    o=(y[3:])
    a=(o[:-5])
    
    

    a15.set(n)
    z=a15.get()
    t=(z[3:])
    q=(t[:-5])
    

    print(i)
    print(a)
    print(q)
    if userid==i and password==a and department==q:
        messagebox.showinfo('Login', 'your are successfully login')
              
        mylist=Listbox(obj,width=110)
        mylist.grid(row=12,column=0,pady=20)
        for line in range(len(w)):
          mylist.insert(END,w[line])
        
        
        department=a3.get()
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        
        c.execute("select * from employeedata where department=?",(department,))
        s=c.fetchall()
        mylist=Listbox(obj,width=120)
        mylist.grid(row=14,column=0,pady=50)
        for line in range(len(s)):
          mylist.insert(END,s[line])
        con.commit()
        con.close()

        


        def add():
            obj.destroy()
            import add

        def delete():
            obj.destroy()
            import delete

        def Update():
            obj.destroy()
            import Update
       
        l1=Label(obj,text="your department employee",fg='black',bg='#EE82EE',font=("Times New Roman",14,'bold'))
        l1.grid(row=13,column=0,padx=10)

        b3=Button(obj,text="add",fg="black",bg="#F5DEB3",command=add,font=("Times New Roman",12,'bold'))
        b3.grid(row=10,column=104)

        b4=Button(obj,text="delete",fg="black",bg="#FFE1FF",command=delete,font=("Times New Roman",12,'bold'))
        b4.grid(row=10,column=105)


        b5=Button(obj,text="Update",fg="black",bg="#63B8FF",command=Update,font=("Times New Roman",12,'bold'))
        b5.grid(row=10,column=106)

    else:
        messagebox.showinfo('Error', 'your data is mis-matched')
        
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
   
def home():
    obj.destroy()
    import LoginSignup
    
'''     def password():
        global updatepassword
        updatepassword=a3.get()
        userid=a4.get()
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set password=? where userid=? ",(updatepassword,userid))
        k=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=55,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()
    def NAME():
        global Name
        updatename=a5.get()
        userid=a4.get()
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set Name=? where userid=? ",(updatename,userid))
        k=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=55,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()
    def date():
        global date
        userid=a4.get()
        date=a6.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set dob=? where userid=?",(date,userid))
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
        d=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()
    def qualification():
        global qualification
        userid=a4.get()
        qualification=a8.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set qualification=? where userid=?",(qualification,userid))
        d=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()
    def adress():
        global adress
        userid=a4.get()
        adress=a9.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set adress=? where userid=?",(adress,userid))
        d=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()


    def salary ():
        userid=a4.get()
        salary=a10.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set salary=? where userid=?",(salary,userid))
        d=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()

    def increment():
        global increment
        userid=a4.get()
        increment=a11.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set increment=? where userid=?",(increment,userid))
        d=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()

    def shift():
        global shift
        userid=a4.get()
        shift=a11.get()
    
        import sqlite3
        con=sqlite3.connect("employee_register.db")
        c=con.cursor()
        c.execute("update employeedata set shift=? where userid=?",(shift,userid))
        d=c.fetchall()
        mylist=Listbox(obj,height = 100,width = 120)
        mylist.grid(row=60,column=105)
        for line in range(len(d)):
            mylist.insert(END,d[line])
        con.commit()

   
    
    b3=Button(obj,text="UPDATE PASSWORD",fg="black",bg="white",command=password,font=("Times New Roman",12,'bold'))
    b3.grid(row=44,column=100)
    e3=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a3)
    e3.grid(row=44,column=102)
    
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

    b11=Button(obj,text="Shift",fg="black",bg="white",command=shift,font=("Times New Roman",12,'bold'))
    b11.grid(row=53,column=100)
    e11=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a12)
    e11.grid(row=53,column=102)'''

  
     


      
                

'''l1=Label(obj,text="WELCOME TO LOGIN PORTAL",fg='black',bg='white',font=("Times New Roman",14,'bold'))
l1.grid(row=0,column=10,padx=10)'''


l1=Label(obj,text="ENTER USER ID",fg='#FFBBFF',bg='#000080',font=("Times New Roman",14,'bold'))
l1.grid(row=1,column=0)
e1=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a1)
e1.grid(row=1,column=1)


l2=Label(obj,text="ENTER PASSWORD",fg='#FFBBFF',bg='#000080',font=("Times New Roman",14,'bold'))
l2.grid(row=3,column=0)
e2=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a2)
e2.grid(row=3,column=1)

l3=Label(obj,text="Department",fg='#FFBBFF',bg='#000080',font=("Times New Roman",14,'bold'))
l3.grid(row=4,column=0)
e3=Entry(obj,justify="left",bg="white",bd=5,insertwidth=5,textvariable=a3)
e3.grid(row=4,column=1)





b2=Button(obj,text="Login",fg="black",bg="#C1FFC1",command=enter,font=("Times New Roman",12,'bold'))
b2.grid(row=5,column=1)


b2=Button(obj,text="Clear",fg="black",bg="#0000FF",command=clear,font=("Times New Roman",12,'bold'))
b2.grid(row=8,column=3)

b2=Button(obj,text="manager portal",fg="black",bg="#FFD39B",command=home,font=("Times New Roman",12,'bold'))
b2.grid(row=8,column=2)

obj.mainloop()
