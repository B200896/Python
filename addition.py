from tkinter import*
def addition():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    myText.set(c)
    
root=Tk()
myText=StringVar()
root.geometry("500x500")
root.resizable(0,0)
un1=Label(root,text="number1")
un1.grid(column=0,row=0)
e1=Entry(root,text="")
e1.grid(row=0,column=1)
un2=Label(root,text="number2")
un2.grid(column=0,row=1)
e2=Entry(root,text="")
e2.grid(row=1,column=1)
button1=Button(root,text="ADD",command=addition)
button1.grid(row=4,column=1)
un3=Label(root,text="",textvariable=myText)
un3.grid(column=0,row=6)
root.mainloop()

