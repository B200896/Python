from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
un=Label(root,text="Library Management")
un.grid(row=0,column=1,columnspan=2)
un=Label(root,text="Book Name",height=2)
un.grid(row=1,column=0)
e=Entry(root,text="")
e.grid(row=1,column=1)
un=Label(root,text="Book ISBN code",height=2)
un.grid(row=2,column=0)
e=Entry(root,text="")
e.grid(row=2,column=1)

un=Label(root,text="Book Author Name",height=2)
un.grid(row=3,column=0)
e=Entry(root,text="")
e.grid(row=3,column=1)
un=Label(root,text="Book Id No.",height=2)
un.grid(row=4,column=0)
e=Entry(root,text="")
e.grid(row=4,column=1)
un=Label(root,text="Availaible Books",height=2)
un.grid(row=5,column=0)
e=Entry(root,text="")
e.grid(row=5,column=1)
un=Button(root,text="NEXT")
un.grid(columnspan=2)
root.mainloop()
row=1
