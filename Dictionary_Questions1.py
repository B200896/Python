'''Method to create Empty Dictionary
There are two ways to create an empty dictionary which are as follows

A = { } # A is an empty dictionary
A = dict( ) # dict( ) method will create an empty dictionary.'''
'''Method to create Dictionary at run time :
Q1. Write a program to enter roll number and names of five students and store the data in dictionary.'''
'''d = { }
for i in range(5):
     rno=int(input("Enter roll number"))
     name=input("Enter name of student")
     d[rno] = name
print(d)'''
'''Q2. Write a program to store book id, book name and price of three books and store the data in dictionary named “dict”'''
dict = {}
for i in range(1):
     b_id = int(input("Enter book id : "))
     b_name = input("Enter book name : ")
     b_price = int(input("Enter price of book : "))
     temp=[b_name,b_price]
     dict[b_id] = temp
print(dict)
#Removing an element from a Dictionary
'''There are two ways by which we can delete the elements of dictionary:

1.By using del statement :

Syntax of using del statement is : del <dictionary-name>[key of element]'''

B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
#del B[2] # It will remove the element of key 2
#print(B)


B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
#del B[3]  # It will return an error (KeyError) if the key given is not present in the dictionary
#print(B)


'''2. By Using pop() function : This function not only delete the element of required key but also return the deleted value.'''

B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
a=B.pop(2) #It returns the element of Key - 2
print("pop",a)
print(B)

B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
a=B.pop(6) #It returns the element of Key - 6
print(a)
print(B)

'''fromkeys()
It will return specified keys and values from the dictionary.
It accepts two parameters.
The first is keys which is mandatory whereas values are optional.
The default value is None.'''

n=int(input("How many customers?"))
l=[]
for i in range(n):
    v=input("Enter names:")
    l.append(v)
d=dict.fromkeys(l,2500)
print(d)

