#dict()Constructor
'''
Employee1=dict(name='John',salary=10000,age=24)
print("Employee1",Employee1)
Employee2=dict({'name':'john','salay':100000,'age':24})
print(Employee2)
Employee3=dict(zip(('name','salary','age'),('John',1000,24)))
print(Employee3)
Employee4=dict([['name','John'],['salary',1000],['age',24]])
print(Employee4)
Employee5=dict((('name','john'),('salary',1000),('age',24)))
print(Employee5)
#Employee6=dict((('name','john'),['salary',1000],('age',24)))
#print("Employee6",Employee6)'''

a={"rollNo":[11,12,13],
   "name":["Teena","Meena","Sita"]
   }
print(a)

b={"rollNo":(11,12,13),
   "name":["Teena","Meena","Sita"]
   }
print(b)
c={("name","add"):["teena","prata"]}
print(type(c))
print(c[("name","add")])
#d={[1,2]:("t","u")}
#print(d)
'''Q1.Write a Program to read roll numbres
and marks of four students and create a dictionay
from it having roll numbers as keys'''
d={}
n=int(input("how many students?"))
#rno=[]
#mks=[]
for a in range(n):
    r=eval(input("enter RollNo"))
    #print(type(r))
    m=eval(input("Marks:"))
    #rno.append(r)
    #mks.append(m)
    d[r]=m
print("Created dictionary",d)
#print(rno)
#print(mks)
#Updating elements in a dictionary--existing key
print("To modify marks")
r=int(input("enter rollnumbers"))
if r in d:
    d[r]=int(input("enter new marks"))
else:
    print("No such roll numberfound")
print("Modified dictionary is")
print(d)
#adding elements in dictionary---no existing of key
while True:
    ans=input(("enter details of new students---y/N"))
    if ans=='y':
        r=int(input("enter new roll no:"))
        m=int(input("enter marks"))
        d[r]=m
    else:
        break
print("dictionary after adding new students")
print(d)
#deleting a dictionary and dictionary element--existing of key
while True:
    c=input("do you want to delete something Y/N:")
    if c=='y':
        r=int(input("roll no to be deleted?;"))
        if r in d:
            del d[r]
            print("Roll No",r,"deleted from dictionary")
        else:
            print("Roll No",r,"does not exist in dictionay")
            
    else:
        break
            
print("after deletion of dictionary")            
print(d)
#some functions
#length function
d={1:'a',2:'c',3:[1,2,3,4]}
print("length",len(d))
#Access elements-->getmethod
print("get method for access element=",d.get(1))
print("get method for access element=",d.get(5,"key is not present"))
#items()
print(d.items())
for a in d.items():
    print(a)
for k,v in d.items():
    print(k,v)

#keys()
print("keys method=",d.keys())
#Values()
print("value method=",d.values())

#update()
emp1={'name:':'john','salary':66000,'age':24}
emp2={'name:':'diya','salary':54000,'age':24,'dept':'salary'}
emp1.update(emp2)
print(emp1)
print("emp2",emp2)
#del
#del emp2
#print(emp2)
#clear
print(emp2.clear())
print(emp2)


                

