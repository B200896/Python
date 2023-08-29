from tkinter import *
t=Tk()
t.geometry("500x500")
s=StringVar()
a=IntVar()
def show():
    if(a.get()==1):
        s.set("pi r^2")
    if(a.get()==2):
        s.set("lxl")


r1=Radiobutton(text="CIRCLE",variable=a,value=1,command=show)
r1.pack()
r2=Radiobutton(text="SQUARE",variable=a,value=2,command=show)
r2.pack()
e1=Entry(textvariable=s)
e1.pack()

root.mainloop()
