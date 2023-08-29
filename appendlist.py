l1=[ ]
for a in range(0,4):
    l1.append(int(input("enter the value:")))
    
print(l1)

n=int(input("enter the no."))
count=0
for i in range(0,len(l1)):  

   if l1[i]==n:
       count=0
       break
   else:
        count=1

if count==0:
    print("number found")
else:
    print("number not found")

    


    

    
