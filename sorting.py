L1=[50,25,5,20,10]
for a in range(0,len(L1)-1):
    for j in range(0,len(L1)-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print(L1)
