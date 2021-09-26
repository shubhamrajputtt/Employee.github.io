from tkinter import *
top=Tk()
top.geometry('500x500')
top.title('EMPLOYEE PORTAL')
top.configure(background='#54FF9F')

f = ("Times bold", 14)

def nextPage():
    top.destroy()
    import LOGIN
def prevPage():
    top.destroy()
    import SIGNUP


Label(top,text=" EMPLOYEE DETAILS",font=20,fg='#EE0000').pack(padx=100 ,pady=100)
    
Button(top,text="LOG IN",font=14,command=nextPage,bg='#8470FF').pack(fill='both',padx=50 ,pady=80)
Button(top,text="SIGN UP",font=14,command=prevPage,bg='#FF00FF').pack(fill='both',padx=50 ,pady=90)
top.mainloop()
