
#RUN time
list1=[]#empty
n=int(input("enter the number"))
for i in range(0,n,1):
  list1.append(input("enter natural number"))
for i in list1:
   print(i)


'''list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
  print(i)'''

'''
a="human"
b=list(a)
print(b)
print(a)

for e in a:
    print(e)


list1=[]
for h in "human":
    list1.append(h)


print(list1)
'''
n=int(input("enter number "))
m=[]

for i in range(0,n,1):
     m.append(int(input("enter values")))
     

print(m)
print(sum)
print("total value=",sum(m))


'''
import numpy as np
l=list()
print("empty list",l)
l6=[2,4,5,6,7]
print("last elements",l6[4])
l1=[]
print("empty list2",l1)
#l2=list(0)
#print(l2)
#l3=list(empty)
#print(l3)
L5=[1,[3,5],7]
print("Nested list",L5[1][0])
print(L5)
thislist=["apple","banana","Cherry"]
print(thislist)
#Access items
print(thislist[1])
#Change item value
thislist[1]="Orange"
print(thislist)
#print list with help of for loop
thislist=["apple","banana","cherry"]
for x in thislist:
    print(x)
       
print(len(thislist))      
        
                     
#appendlist
thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

    
#
'''

L=[1,2,3]
a=L*3
print(a)

N=np.array([1,2,3,4,5])
a=N*3
print(a)

A=np.array([10,20,30,40,50,60,70,80,90])
B=np.array([[0,1,2,3],
[4,5,6,7],
[8,9,10,11],
[12,13,14,15]])
              
print(B[0:2,1:3])



