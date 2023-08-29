l1=[ ]
for a in range(0,4):
   l1.append(int(input("Enter the list")))
   
print(l1)
n=int(input("Enter the no "))
count=0
for i in range(0,len(l1)):
      if l1[i]==n:        
        count+=1
print("search element count",count)
         
