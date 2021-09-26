from tkinter import *

L = Tk()
L.geometry('800x800')
L.title('Python company')
L['bg']='#5d8a82'



def nextPage():
    L.destroy()
    import managerlogin

def nextPage1():
    L.destroy()
    import managersignup

def home():
    L.destroy()
    import home_page   
    


Label(L,text="Welcome to manager portal",font=("Times New Roman",30,'bold'),fg='#FF6347').pack(padx=100, pady=100)

Button(L,text="LoginPage",font=14,command=nextPage,bg='#7D9EC0').pack(padx=50, pady=10,fill=X)
Button(L,text="SignupPage",font=14,command=nextPage1,bg='#FF8247').pack(padx=50, pady=20,fill=X)
Button(L,text="Homepage",font=14,command=home,bg='#C6E2FF').pack(padx=50, pady=30)

L.mainloop()
