from tkinter import*


def add_numbers():
    res=int(e1.get())+int(e2.get())
    myText.set(res)
    
    
window=Tk()
window.title("CAL_C")
myText=StringVar()

Label(window,text="first number").grid(row=0,sticky=W)
Label(window,text="second number").grid(row=1,sticky=W)
Label(window,text="result of addition:").grid(row=3,sticky=W)
result=Label(window,text="",textvariable=myText).grid(row=3,column=1,sticky=W)

e1=Entry(window)# e1 is the object of this program
e2=Entry(window)# e2 is the object of this program

e1.grid(row=0,column=1) #place e1 in row 0 and column 1
e2.grid(row=1,column=1) #place e2 in row 1 and column 2

b=Button(window,text="Calculate",command=add_numbers)
#b is the object from the button class, preform click event by calling addNumbers() 
b.grid(row=0,column=2,columnspan=2, rowspan=2, sticky=W+E+N+S,padx=5,pady=5)


window.mainloop()
