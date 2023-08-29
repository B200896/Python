from tkinter import *
window=Tk()
window.geometry("1000x600")

#------------------------------------------------------------------addBooks------------------------------------------------------------------
def addBooks():
    from tkinter import messagebox
    import mysql.connector

    global id
    global title
    global Class
    global author
    f2=Frame(bg="white")
    f2.place(x=0,y=0,width=1000,height=600)
    window.title('Library Management System')
 
    greet = Label(window, font = ('arial', 30, 'bold'), text = "Add Books")
    greet.place(relx=0.5,rely=0.1,anchor='center')
 
    #----------id-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.place(relx=0.355,rely=0.2,anchor='center')
 
    id=Entry(window,width=20,font =('arial', 15, 'bold'))
    id.place(relx=0.55,rely=0.2,anchor='center')
 
    #----------title-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Title: ")
    L.place(relx=0.37,rely=0.3,anchor='center')
 
    title=Entry(window,width=20,font =('arial', 15, 'bold'))
    title.place(relx=0.55,rely=0.3,anchor='center')
 
    #----------Class-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Class: ")
    L.place(relx=0.37,rely=0.4,anchor='center')
 
    Class=Entry(window,width=20,font =('arial', 15, 'bold'))
    Class.place(relx=0.55,rely=0.4,anchor='center')
    
    #----------author-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Author: ")
    L.place(relx=0.36,rely=0.5,anchor='center')
 
     
    author=Entry(window,width=20,font =('arial', 15, 'bold'))
    author.place(relx=0.55,rely=0.5,anchor='center')
    
    submitbtn2=Button(window,text="summit",command=add_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn2.place(relx=0.5,rely=0.6,anchor='center')

    Backbtn2=Button(window,text="Back",command=home,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    Backbtn2.place(relx=0.05,rely=0.05,anchor='center')


#------------------------------------------------------------------deleteBooks------------------------------------------------------------------
def DeleteBooks():
    from tkinter import messagebox
    import mysql.connector
 
    global id
    f3=Frame(bg="white")
    f3.place(x=0,y=0,width=1000,height=600)
    window.title('Library Management System')
 
    greet = Label(window,bg='blue', font = ('arial', 30, 'bold'), text = "Delete Books")
    greet.place(relx=0.5,rely=0.1,anchor='center')
 
    #----------id-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.place(relx=0.355,rely=0.2,anchor='center')
 

    id=Entry(window,width=20,font =('arial', 15, 'bold'))
    id.place(relx=0.55,rely=0.2,anchor='center')

    back=Button(window,text="Back",command=home,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    back.place(relx=0.05,rely=0.05,anchor='center')
 
    submit=Button(window,text="Submit",command=delete_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submit.place(relx=0.5,rely=0.3,anchor='center')


#------------------------------------------------------------------IssueBooks------------------------------------------------------------------
def Issue():
    from tkinter import messagebox
    import mysql.connector

    global id
    global StudentName
    global Class
    
    f4=Frame(bg="white")
    f4.place(x=0,y=0,width=1000,height=600)
    
    window.title('Library Management System')
 
    greet = Label(window, font = ('arial', 30, 'bold'), text = "Issue Books")
    greet.place(relx=0.5,rely=0.1,anchor='center')
 
    #----------id-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.place(relx=0.355,rely=0.2,anchor='center')
 
    id=Entry(window,width=20,font =('arial', 15, 'bold'))
    id.place(relx=0.55,rely=0.2,anchor='center')
 
    #----------StudentName-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter StudentName: ")
    L.place(relx=0.33,rely=0.3,anchor='center')
 
    StudentName=Entry(window,width=20,font =('arial', 15, 'bold'))
    StudentName.place(relx=0.55,rely=0.3,anchor='center')

    #----------Class-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Class: ")
    L.place(relx=0.37,rely=0.4,anchor='center')
 
    Class=Entry(window,width=20,font =('arial', 15, 'bold'))
    Class.place(relx=0.55,rely=0.4,anchor='center')
    
    submitbtn=Button(window,text="Submit",command=issue_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.place(relx=0.5,rely=0.5,anchor='center')

    back=Button(window,text="Back",command=home,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    back.place(relx=0.05,rely=0.06,anchor='center')


#------------------------------------------------------------------ReturnBooks------------------------------------------------------------------
def Return():
    from tkinter import messagebox
    import mysql.connector
    global id
    
    f5=Frame(bg="white")
    f5.place(x=0,y=0,width=1000,height=600)

    window.title('Library Management System')
 
    greet = Label(window, font = ('arial', 30, 'bold'), text = "Return Books")
    greet.place(relx=0.5,rely=0.1,anchor='center')
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.place(relx=0.355,rely=0.2,anchor='center')
 
    id=Entry(window,width=20,font =('arial', 15, 'bold'))
    id.place(relx=0.55,rely=0.2,anchor='center')
 
    back=Button(window,text="Back",command=home,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    back.place(relx=0.05,rely=0.05,anchor='center')
 
    submit=Button(window,text="Submit",command=return_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submit.place(relx=0.5,rely=0.3,anchor='center')


#------------------------------------------------------------------ViewBooks------------------------------------------------------------------
def View():
    from tkinter import messagebox
    import mysql.connector
    f5=Frame(bg="white")
    f5.place(x=0,y=0,width=1000,height=600)
    
    window.title('Library Management System')
 
    greet = Label(window, font = ('arial', 30, 'bold'), text = "View Books")
    #greet.place(relx=0.5,rely=0.1,anchor='center')
    greet.grid(row = 0,columnspan = 2,column=1)

    back=Button(window,text="Back",command=home,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    back.place(relx=0.05,rely=0.05,anchor='center')
   
 
    db = mysql.connector.connect(host ="localhost",user = "Devendra",password = 'dhaked',database='db')
    cursor = db.cursor()
 
    sqlquery= "select * from Books ;"
    print(sqlquery)
 
    try:
        cursor.execute(sqlquery)
 #      db.commit()
        L = Label(window, font = ('arial', 15), text = "%-10s%-15s%-15s%-15s%-10s"%(' BID ',' Title ',' Author ',' Available ',' Class '))
       # L.place(relx=0.5,rely=0.2,anchor='center')
        L.grid(row = 1,columnspan = 2,column=1)

 
        L = Label(window, font = ('arial', 30), text = "---------------------------------------------------------------------------")
        #L.place(relx=0.5,rely=0.3,anchor='center')
        L.grid(row = 2,columnspan = 4)
 
        X=4
        for i in cursor:
            L = Label(window, font = ('arial', 15), text = "%-10s%-20s%-20s%-20s%-10s"%(i[0],i[1],i[2],i[3],i[4]))
            #L.place(relx=0.5,rely=X,anchor='center')
            L.grid(row = X,columnspan = 4)
            X+=1
 
    except:
        messagebox.showinfo("Error","Cannot Fetch data.")


#------------------------------------------------------------------Home------------------------------------------------------------------    
def home( ):    
    f1=Frame(bg="white")
    f1.place(x=0,y=0,width=1000,height=600)
    window.title("Library Management System")
 
    greet = Label(window,bg='blue', font = ('arial', 30, 'bold'), text = "Welcome to Library Management System")
    greet.place(relx=0.5,rely=0.1,anchor='center')
    
    #-------------Add Book---------------
    addbtn=Button(window,text="  Add Books ",command=addBooks,bg="yellow",fg="white",font = ('arial', 20, 'bold'))
    addbtn.place(relx=0.5,rely=0.2,anchor='center')
    
    #-------------Delete Book------------
    deletebtn=Button(window,text="Delete Books",command=DeleteBooks,bg="yellow",fg="white",font = ('arial', 20, 'bold'))
    deletebtn.place(relx=0.5,rely=0.3,anchor='center')

    #-------------Issue Book-------------
    issuebtn=Button(window,text="Issue  Books",command=Issue,bg="yellow",fg="white",font = ('arial', 20, 'bold'))
    issuebtn.place(relx=0.5,rely=0.4,anchor='center')
    
    #-------------Return Book------------  
    returnbtn=Button(window,text="Return Books",command=Return,bg="yellow",fg="white",font = ('arial', 20, 'bold'))
    returnbtn.place(relx=0.5,rely=0.5,anchor='center')
    
    #-------------View Book--------------
    viewbtn=Button(window,text=" View Books  ",command=View,bg="yellow",fg="white",font = ('arial', 20, 'bold'))
    viewbtn.place(relx=0.5,rely=0.6,anchor='center')
 
    greet = Label(window,bg= 'black',fg='white',font = ('arial', 20, 'bold'), text = "Thank you")
    greet.place(relx=0.5,rely=0.7,anchor='center')


#------------------------------------------------------------------add_db------------------------------------------------------------------    
def add_db():
    from tkinter import messagebox
    import mysql.connector
    
    global id
    global title
    global author
    global Class
 
    bid=id.get()
    btitle=title.get()
    bauthor=author.get()
    bClass=Class.get()
    
    db = mysql.connector.connect(host ="localhost",user = "Devendra",password = 'dhaked',database='db')
    cursor = db.cursor()
       
    print(bid,end='--')
    print(btitle,end='--')
    print(bClass,end='--')
    print(bauthor,end='--')
    print("add")
 
    sqlquery= "insert into books values('" + bid +"','"+btitle+"','"+bauthor+"','YES','"+bClass+"');"
    print(sqlquery)
 
    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Book added Successfully")
        
    except:
        messagebox.showinfo("Error","Cannot add given book data into Database")
        
    
    window.destroy()


#------------------------------------------------------------------delete_db------------------------------------------------------------------
def delete_db():
    from tkinter import messagebox
    import mysql.connector
 
    global id
 
    bid=id.get()
    
    db = mysql.connector.connect(host ="localhost",user = "Devendra",password = 'dhaked',database='db')
    cursor = db.cursor()
    
    print(bid,end='--')
    print("delete")
 
    sqlquery= "delete from books where bid='"+bid+"';"
    print(sqlquery)
 
    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Book deleted Successfully")
    except:
        messagebox.showinfo("Error","Book with given id does not exist")
    
    window.destroy()


#------------------------------------------------------------------issue_db------------------------------------------------------------------    
def issue_db():
    from tkinter import messagebox
    import mysql.connector
    
    global id
    global StudentName
    global Class
 
    bid=id.get()
    bStudentName=StudentName.get()
    bClass=Class.get()
 
    db = mysql.connector.connect(host ="localhost",user = "Devendra",password = 'dhaked',database='db')
    cursor = db.cursor()
    
    print(bid,end='--')
    print(bStudentName,end='--')
    print(bClass,end='--')
    print("issue")
 
    try:
        checkavailability=" select * from books where available='YES';"
        print(checkavailability)
        cursor.execute(checkavailability)
 
        flag=0
 
        for i in cursor:
            print(i[0])
            if(i[0]==bid):
                flag=1
                break;
        
        if flag==1:     
            updatequery="update books set available='NO' where bid='"+bid +"';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()
 
            sqlquery= "insert into issue values('" + bid +"','" +bStudentName+"' ,'"+bClass+"');"
            print(sqlquery)
 
            cursor.execute(sqlquery)
            db.commit()
 
            messagebox.showinfo('Success',"Book issued Successfully")
        else:
            messagebox.showinfo("Error","Required Book is not available")
    except:
        messagebox.showinfo("Error","Cannot issue given book ")


#------------------------------------------------------------------return_db------------------------------------------------------------------
def return_db():
    from tkinter import messagebox
    import mysql.connector
 
    global id
 
    bid=id.get()
 
    db = mysql.connector.connect(host ="localhost",user = "Devendra",password = 'dhaked',database='db')
    cursor = db.cursor()
    
    print(bid,end='--')
    print("return")
 
    try:
        checkavailability=" select * from books where available='NO';"
        print(checkavailability)
        cursor.execute(checkavailability)
 
        flag=0
 
        for i in cursor:
            print(i[0])
            if(i[0]==bid):
                flag=1
                break;
        
        if flag==1:     
            updatequery="update books set available='YES' where bid='"+bid +"';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()
 
            sqlquery= "delete from issue where bid='" + bid +"';"
            print(sqlquery)
 
            cursor.execute(sqlquery)
            db.commit()
 
            messagebox.showinfo('Success',"Book returned Successfully")
        else:
            messagebox.showinfo("Error","Invalid Book id")
    except:
        messagebox.showinfo("Error","Cannot return given book ")
home()
