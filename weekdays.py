from tkinter import*
root=Tk()
root.geometry("500x500")

s=StringVar()
a=IntVar()
def show():
    if(a.get()==1):
        s.set("Monday")
    if(a.get()==2):
        s.set("Tuesday")
    if(a.get()==3):
        s.set("Wednesday")
    if(a.get()==4):
        s.set("Thursday")
    if(a.get()==5):
        s.set("Friday")
    if(a.get()==6):
        s.set("Saturday")
    if(a.get()==7):
        s.set("Sunday")
r1=Radiobutton(text="1",variable=a,value=1,command=show)
r1.pack()
r2=Radiobutton(text="2",variable=a,value=2,command=show)
r2.pack()
r3=Radiobutton(text="3",variable=a,value=3,command=show)
r3.pack()
r4=Radiobutton(text="4",variable=a,value=4,command=show)
r4.pack()
r5=Radiobutton(text="5",variable=a,value=5,command=show)
r5.pack()
r6=Radiobutton(text="6",variable=a,value=6,command=show)
r6.pack()
r7=Radiobutton(text="7",variable=a,value=7,command=show)
r7.pack()
e1=Entry(textvariable=s)
e1.pack()

root.mainloop()








    
    
    
