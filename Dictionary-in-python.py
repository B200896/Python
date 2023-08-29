
#creating dictionary

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)

# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)

# from sequence having each item as a pair
my_dict = dict([(12,'Red'), (20,'Green')])

print(my_dict)

#access elements  ******************
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])
print(my_dict['age'])

# Output: 26
print(my_dict.get('age'))

#Add or Change  ****************

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = '258,Katewa Nagar'
my_dict['city'] = 'jaipur' 
print(my_dict)
# Output: {'city':'jaipur', 'address': 'Downtown', 'age': 27, 'name': 'Jack'}
'''
print(my_dict.pop('address'))
print(my_dict)
del my_dict['city']
print(my_dict)
'''
#Membership Test
print('Membership')
print('age' in my_dict)

#Get Keys
for i in my_dict:
    print (i,' ',end='')
print()
#Get Values
for i in my_dict:
    print (" at Key ",i,'Value is ',my_dict[i])

print('*******************')
for x,y in thisdict.items():
  print(x,y)

print('*******************')
for x in thisdict.values():
  print(x)

  
#functions

squares = {1: 1, 3: 9, 5: 25,  9: 41,7: 49}

# Output: 5
print(len(squares))

#sort by key
# Output: [1, 3, 5, 7, 9]
print('sorted ',sorted(squares))
print('Original ',squares)

#sort by value
print('Sorted Items')
import operator

sorted_squares = sorted(squares.items(), key=operator.itemgetter(1))
print('Sort on values ',sorted_squares)

sorted_squares = sorted(squares.items(), key=operator.itemgetter(0))
print('Sort on keys ',sorted_squares)

s1=dict(sorted(squares.items(), key=lambda x: x[1]))
#s1 = sorted(squares.items(), key=lambda value: value[1])
print(s1)

print(squares[9])


#
for x in squares.values():
  print(x)  


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

  

thisdict.popitem()  #remove last item
print(thisdict)


