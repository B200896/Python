list1=[]
for s in range(0,3):
    for a in range(1):
        list1.append([])
        z=int(input("Enter term:"))
        for b in range(z):
            x=int(input("Enter value:"))
            list1[s].append(x)
print(list1)
