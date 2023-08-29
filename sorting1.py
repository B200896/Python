L1=[50,25,5,20,10]
for a in range(0,len(L1)-1):
    for j in range(0,len(L1)-1):
        if L1[j]>L1[j+1]:
            temp=L1[j]
            L1[j]=L1[j+1]
            L1[j+1]=temp

print(L1)
print(L1[4])

