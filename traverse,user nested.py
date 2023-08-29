list2=[[1,2],[3,30,333],[11]]
for j in list2:
    for k in j:
        print(k)
##traversing
list2=[]
for j in range(3):
    list2.append([])
    for a in range(2):
        x=int(input("Enter the value of list"))
        list2[j].append(x)
        break
    for a in range(3):
        x=int(input("Enter the value of list"))
        list2[j].append(x)
        
    
    print(list2)
