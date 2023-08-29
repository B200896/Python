import mysql.connector as sqLtor
mycon=sqLtor.connect(host="localhost",user="root",passwd="Admin@123",database="library9")
if mycon.is_connected():
    print("Successfully Connected to MYSQL database")

    Result_set=mycon.cursor();
    r=int(input("enter student_id"))
    s=input("enter student Branch")
    y=int(input("enter roll no"))
    s_name=input("enter Name")
    Mob_no=int(input("enter mobile"))
    query="insert into student9 values(%s,'%s',%s,'%s',%s)" %(r,s,y,s_name,Mob_no)
    #query="update student set salary=%s where Roll_No=%s" %(sal,r)
    #query1="DELETE from student where s_name='%s'" %(s)
    #query2="update student set salary=%s where s_name='%s'" %(sal,s)
    
    Result_set.execute(query)
    '''
    data=Result_set.fetchall()
    for a in data:
        print(a)
    '''
    mycon.commit()#changes in done database should be apply
    #print("Row inserted successfully")
    print("Row updated successfully")
    mycon.close()#close the connection
    print("database is close")
    
else:
    
    print("not connected")

