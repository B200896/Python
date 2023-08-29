from tkinter import *
root=Tk()
mytext=StringVar()
root.geometry("500x500")
root.resizable(0,0)

def show():
    #print("hello")
    mytext.set("hello")


b1=Button(root,text="OK",command=show)
b1.pack()
u=Label(root,textvariable=mytext)
u.pack()

root.mainloop()
