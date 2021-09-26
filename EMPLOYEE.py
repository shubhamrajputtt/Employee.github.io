from tkinter import *
top=Tk()
top.geometry('400x300')
top.title('EMPLOYEE PORTAL')
top.configure(background='#00FF00')

f = ("Times bold", 14)

def nextPage():
    top.destroy()
    import NOTICEBOARD
def prevPage():
    top.destroy()
    import PERSONALDETAILS
def home():
    top.destroy()
    import home_page



Label(top,text="WELCOME TO EMPLOYEE PORTAL",font=150,fg="#1E90FF").pack(padx=50 ,pady=100)
    
Button(top,text="NOTICE BOARD",font=14,command=nextPage,bg="#FCE6C9").pack(fill='both',padx=50 ,pady=20)
Button(top,text="PERSONEL DATA",font=14,command=prevPage,bg="#F08080").pack(fill='both',padx=50 ,pady=30)
Button(top,text="Back to home page",font=14,command=home,bg="#FF83FA").pack(padx=50 ,pady=40)
top.mainloop()
