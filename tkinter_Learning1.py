from tkinter import *
root=Tk()
#root.minsize(600,600)
#root.maxsize(600,600)
root.geometry("500x500")
root.resizable(0,0)
'''
un=Label(root,text="Resgistration\nForm",font=("Arial",25),bg="red",fg="white",width="15",height="2")
un.pack()

un=Entry(root,font=("Arial",20),fg="Black",width="10",bg="White")
un.pack()

un=Button(root,font=("Arial",20),fg="Black",width="10",bg="White",text="CLICK")
un.pack()
'''
un=Label(root,text="NAME",font=("Arial",20),bg="Black",fg="white",width="15",height="1")
un.grid(row=0,column=0,pady=25,sticky=W)
e1=Entry(root,font=("Arial",20),fg="Black",width="10",bg="White")
e1.grid(row=0,column=1)
up=Label(root,text="AGE",font=("Arial",20),bg="Black",fg="white",width="15",height="1")
up.grid(row=1,column=0,pady=25)
e2=Entry(root,font=("Arial",20),fg="Black",width="10",bg="White")
e2.grid(row=1,column=1)
root.mainloop()
print("hello")
