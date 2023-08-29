import mysql.connector as sql1
mycon=sql1.connect(host="localhost",user="root",passwd="Admin@123",database="school")
print("mycon",mycon)
if mycon.is_connected():
    print("connected")
    Result_set=mycon.cursor();
    print("ResultSet",Result_set)
    query1="select * from student"

    Result_set.execute(query1)
    data=Result_set.fetchall()
    for a in data:
        print(a)
        

else:
    print("not connected")
