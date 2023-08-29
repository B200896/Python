from tkinter import*
root=Tk()
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
root.mainloop()

