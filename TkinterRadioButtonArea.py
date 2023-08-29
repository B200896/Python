from tkinter import *
root=Tk()
root.geometry("500x500")
s=StringVar()
t=StringVar()
a=IntVar()
def show():
    radius=10
    Length=20
    Width=10
    Side=100
    if(a.get()==1):
        circle=3.14*radius*radius
        t.set("Circle ")
        s.set(circle)
    if(a.get()==2):
        rectangle=Length*Width
        t.set("Rectangle ")
        s.set(rectangle)
    if(a.get()==3):
        square=Side*Side
        t.set("Square ")
        s.set(square)

r1=Radiobutton(text="Circle",variable=a,value=1,command=show)
r1.pack()
r2=Radiobutton(text="Rectangle",variable=a,value=2,command=show)
r2.pack()
r3=Radiobutton(text="Square",variable=a,value=3,command=show)
r3.pack()
e1=Entry(textvariable=t)
e1.pack()
e2=Entry(textvariable=s)
e2.pack()
root.mainloop()
