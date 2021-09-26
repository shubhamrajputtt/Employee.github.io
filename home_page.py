from tkinter import *
top=Tk()
top.geometry('900x800')
top.title('python company')
top.configure(background='yellow')

def nextPage():
    top.destroy()
    import LoginSignup
    
def prevPage():
    top.destroy()
    import EMPLOYEE

def exitpage():
    top.destroy()
    
    


Label(top,text="WELCOME TO PYTHON COMPANY",fg='blue',font=150).pack(padx=50 ,pady=100)

Button(top,text="MANAGER",font=14,bg='green',command=nextPage).pack(fill=BOTH,padx=50 ,pady=20)
Button(top,text="EMPLOYEE",font=14,bg='pink',command=prevPage).pack(fill=BOTH,padx=50 ,pady=30)
Button(top,text="EXIT",font=14,bg='RED',command=exitpage).pack(padx=50 ,pady=40)    




top.mainloop()
