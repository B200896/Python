import mysql.connector as proj
mycon=proj.connect(host="localhost",user="root",passwd="Admin@123",database="library9")
if mycon.is_connected():
    print("successfully connected")
    Result_set=mycon.cursor();
    '''
    r=int(input("enter student_id"))
    s=input("enter student Branch")
    y=int(input("enter roll no"))
    s_name=input("enter Name")
    Mob_no=int(input("enter mobile"))
    '''
    s_name_new=input("enter New Name ")
    s_name_old=input("enter old Name")
    #query="insert into student9 values(%s,'%s',%s,'%s',%s)" %(r,s,y,s_name,Mob_no)
    query2="update student9 set st_Name='%s' where st_Name='%s'" %(s_name_new,s_name_old)
 
    Result_set.execute(query2)
    mycon.commit()
     #print("Row updated successfully")
    mycon.close()#close the connection
    print("database is close")
    
