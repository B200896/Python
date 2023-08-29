from tkinter import*
t=Tk()
t.geometry("500x500")
f2=Frame(bg="white")

f2.place(x=0,y=0,width=1000,height=600)

#greet = Label(window, font = ('arial', 30, 'bold'), text = "Add Books")
#greet.place(relx=0.5,rely=0.1,anchor='center')
'''def Add1():
    import mysql.connector as proj
    mycon=proj.connect(host="localhost",user="root",passwd="Admin@123",database="project")
    if mycon.is_connected():
        #print("successfully connected")
        Result_set=mycon.cursor();
        print("hello")
        B_name=e1.get()
        B_id=int(e2.get())
        B_Au=e3.get()
        B_isbn=int(e4.get())
        B_s=int(e5.get())   
        
        query="insert into bookss values('%s',%s,'%s',%s,%s)" %(B_name,B_id,B_Au,B_isbn,B_s)
        #query2="update student9 set st_Name='%s' where st_Name='%s'" %(s_name_new,s_name_old)
     
        Result_set.execute(query)
        mycon.commit()
        print("New Record Added")
        mycon.close()#close the connection
        print("database is close")
        



    else:
        print("not connected")
'''
def Add ():
    f2=Frame()
    f2.place(x=0,y=0,width=425,height=400)
    u=Label(f2,text="ADD BOOKS")
    u.place(x=220,y=20)
    u1=Label(f2,text="book name")
    u1.place(x=100,y=80)
    e1=Entry(f2,font=("",12))
    e1.place(x=200,y=80,width=120)
    u2=Label(f2,text="Book ID")
    u2.place(x=100,y=130)
    e2=Entry(f2,font=("",12))
    e2.place(x=200,y=130,width=120)
    u3=Label(f2,text="Book Auther Name")
    u3.place(x=80,y=180)
    e3=Entry(f2,font=("",12))
    e3.place(x=200,y=180,width=120)
    u4=Label(f2,text="Book ISBN code")
    u4.place(x=100,y=230)
    e4=Entry(f2,font=("",12))
    e4.place(x=200,y=230,width=120)
    u5=Label(f2,text="BOOK STATUS")
    u5.place(x=100,y=280)
    e5=Entry(f2,font=("",12))
    e5.place(x=200,y=280,width=120)
    

    def Add_in_db():
        B_name=e1.get()
        print(B_name)
        B_id=int(e2.get())
        print(B_id)
        B_Au=e3.get()
        print(B_Au)
        B_isbn=int(e4.get())
        print(B_isbn)
        B_s=int(e5.get())
        print(B_s)
        import mysql.connector as proj
        mycon=proj.connect(host="localhost",user="root",passwd="Admin@123",database="project")
        if mycon.is_connected():
            #print("successfully connected")
            Result_set=mycon.cursor();
            query="insert into bookss values('%s',%s,'%s',%s,%s)" %(B_name,B_id,B_Au,B_isbn,B_s)
       
            Result_set.execute(query)
            mycon.commit()
            print("New Record Added")
            mycon.close()#close the connection
            print("database is close")
        


        
    b3=Button(f2,text="Submit",command=Add_in_db)
    b3.place(x=210,y=320,width=100)
    b2=Button(f2,text="back",command=home)
    b2.place(x=2,y=3)
    
    '''b3=Button(f2,text="Login")
    b3.place(x=100,y=380,width=200)'''
def delete():
    f3=Frame()
    f3.place(x=0,y=0,width=425,height=480)
    
    u=Label(f3,text="DELETED BOOKS")
    u.place(x=200,y=20)
    u4=Label(f3,text="Book ID")
    u4.place(x=100,y=100)
    e4=Entry(f3,font=("",12),show='*')
    e4.place(x=180,y=100,width=120)
    b2=Button(f3,text="Back",command=home)
    b2.place(x=2,y=3)
    b3=Button(f3,text="Delete Books")
    b3.place(x=150,y=200,width=120)
#
def Issue():
    f4=Frame()
    f4.place(x=0,y=0,width=425,height=280)
    u=Label(f4,text="Issue Books List")
    u.place(x=180,y=40)
    u5=Label(f4,text="Issued Book ID No.")
    u5.place(x=70,y=80)
    e5=Entry(f4,font=("",12),show='*')
    e5.place(x=180,y=80,width=120)
    u6=Label(f4,text=" Student Name")
    u6.place(x=70,y=140)
    e6=Entry(f4,font=("",12),show='*')
    e6.place(x=180,y=140,width=120)
    u7=Label(f4,text=" Student Branch")
    u7.place(x=70,y=110)
    e7=Entry(f4,font=("",12),show='*')
    e7.place(x=180,y=110,width=120)
    u8=Label(f4,text="Date of issue")
    u8.place(x=80,y=165)
    e8=Entry(f4,font=("",12),show='*')
    e8.place(x=180,y=165,width=120)    
    b5=Button(f4,text="Back",command=home)
    b5.place(x=2,y=3)
    b5=Button(f4,text="Done")
    b5.place(x=150,y=200,width=120)
def home( ):

    l1=Label(f1,text="Library system Management")
    l1.place(x=250,y=150,width=160)
    f1=Frame(bg="Black")
    f1.place(x=0,y=0,width=425,height=280)
    b1=Button(f1,text="Add Books",command=Add)
    b1.pack(pady=20)
    f2.place(x=0,y=0,width=425,height=280)
    b2=Button(f1,text="Delete Books",command=delete)
    b2.pack()
    b5=Button(f1,text="Issued Books",command=Issue)
    b5.pack()
    b6=Button(f1,text="Display Records",command=Issue)
    b6.pack()
home()
t.mainloop()
