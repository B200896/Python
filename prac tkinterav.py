from tkinter import*
def average():
 a=int(e1.get())
 b=int(e2.get())
 c=int(e3.get())
 d=int(e4.get())
 m=a+b+c+d%4
 myText.set(m)
root=Tk()
myText=StringVar()
root.geometry("500x500")
root.resizable(0,0)
un1=Label(root,text="English")
un1.grid(row=0,column=0)
e1=Entry(root,text=" ")
e1.grid(row=0,column=1)
un2=Label(root,text="Hindi")
un2.grid(row=1,column=0)
e2=Entry(root,text=" ")
e2.grid(row=1,column=1)
un3=Label(root,text="Maths")
un3.grid(row=2,column=0)
e3=Entry(root,text=" ")
e3.grid(row=2,column=1)
un4=Label(root,text="Science")
un4.grid(row=3,column=0)
e4=Entry(root,text=" ")
e4.grid(row=3,column=1)
b=Button(root,text="average",command=average)
b.grid(row=4,column=1)
e5=Entry(root,textvariable=myText)
e5.grid(row=4,column=2)
root.mainloop()











