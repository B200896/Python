#Q1 Program to print elements of a list['q','w','e','r','t','y'] in separate
#lines along with element's both indexes(positive and negative).
'''
L=['q','w','e','r','t','y']
length=len(L)
for a in range(length):
    print("At indexes",a,"and",(a-length),"elements:",L[a])
'''

#Q2 Extract two list-slices out of a given list of numbers.Display and
#print the sum of elements of first list-slice which contains other elements of
#the list between indexes 5 to 15.Program should also displays the average
#of elements in second list slice that contains every fourth element
#of the list.
#solution
'''
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
slc1=lst[5:15:2]
slc2=lst[::4]
sum=avg=0
print("Slice1")
for a in slc1:
    sum+=a
    print(a,end='')
print()
print("sum of elements of slice1:",sum)
print("Slice2")
sum=0
for a in slc2:
      sum+=a
      print(a,end='')
print()
print("sum of elements of slice2:",slc2)
avg=sum/(len(slc2))
print("Average of elements of slice2:",avg)
'''
#Q3Program to find minimum element from a list of element along with its index in the list
#solution
'''

lst=[]
for a in range(1,11,1):
    lst.append(int(input("enter value")))
print(lst)
length=len(lst)
min_ele=lst[0]
min_index=0
for i in range(1,length-1):
               if lst[i]<min_ele:
                   min_ele=lst[i]
                   min_index=i
print("Given list is:",lst)
print("The minimum element of the given list is:")
print(min_ele,"at index",min_index)
'''               
#Q4.Program to calculate mean of a given list of numbers
'''
lst=[]
for a in range(1,11,1):
    lst.append(int(input("enter value")))
print(lst)
length=len(lst)
mean=sum=0
for i in range(1,length-1):
               sum+=lst[i]
mean=sum/length
print("Given list is:",lst)
print("sum of elements:",sum)
print("The mean of the given list is:",mean)
'''
#Q5 Program to search for an element in a given list of numbers

'''
lst=[]
for a in range(1,5,1):
    lst.append(int(input("enter value")))
print(lst)
length=len(lst)
element=int(input("enter elements to be searched for:"))
flag=0
for i in range(0,length-1):
               if element==lst[i]:
                   flag+=1
                   print(element,"found at index",i)
                   break
        
               else:
                   flag=0
                   #print(element,"not found in given list")

if flag==0:
    print(element,"not found in given list")

'''
#Q6 Program to count frequency of a given element in alist of numbers
'''
lst=[]
for a in range(1,11,1):
    lst.append(int(input("enter value")))
print(lst)
length=len(lst)
print("length",length)
element=int(input("enter elements to be searched for:"))
count=1
for i in range(1,length):
               if element==lst[i]:
                   count=count+1                 
        
               else:
                   count=1

if count==1:
    print(element,"not found in given list")
else:
    print(element,"has frequency as",count,"in given list")
'''
#Q7Program to finf frequencies of all elements of a list.
#Aso,print the list of unique elements in the list and duplicate
#elements in the given list.

lst=[]
for a in range(1,11,1):
    lst.append(int(input("enter value")))
print(lst)
length=len(lst)
uniq=[]
dupl=[]
count=i=0
while i<length:
    element=lst[i]
    count=1
    if element not in uniq and element not in dupl:
        i+=1
        for j in range(i,length):
            if element==lst[j]:
                count+=1
        else:
            print("Element",element,"frequency:",count)
            if count==1:
                uniq.append(element)
            else:
                dupl.append(element)
                #when element is found in uniq or dupl lists
    else:
        i+=1
print("Original list",lst)
print("Unique elements list",uniq)
print("Duplicates elements list",dupl)
