#How to Iterate Through a Dictionary in Python: The Basics
dict1={'NAME':'Meena','Class':1,'Sub':'Math'}
print(dict1)
print(dir({}))
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)
#indexing operator [] with the dictionary and its keys to
#get access to the values:
for key in a_dict:
    print(key, '->', a_dict[key])
#Iterating Through .items()
a_dict1={'colour':'blue','fruit':'apple','pet':'dog'}
print(a_dict1.items())

for item in a_dict.items():
    print(item)
    print(type(item))
for key, value in a_dict.items():
    print(key, '->', value)
#Iterating Through .keys()
#If you just need to work with the keys of a dictionary, then you can use .keys(), which is a method that returns a new view object containing the dictionary’s keys:

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
keys = a_dict.keys()
print(keys)
#Iterating Through .values()
'''It’s also common to only use the values to iterate through a
dictionary in Python. One way to do that is to use .values(),
which returns a view with the values of the dictionary:'''
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
values = a_dict.values()
print(values)
print("*********************************************")
#Modifying Values and Keys
#prices[k] = round(v * 0.9, 2)  # Apply a 10% discount
#prices
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for k, v in prices.items():
    print(k,'->',v)
    print(k,'->',v*2)
    prices[k]=v*2
print(prices)

# Python 3. dict.keys() returns a view object, not a list
#Deletion of Key
'''prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in prices.keys():
    print(key)
    if key == 'orange':
        #del prices[key]
        #del key
#print(prices)'''
#Deletion of key
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in list(prices.keys()):  # Use a list instead of a view
    if key == 'orange':
        del prices[key]  # Delete a key from prices
print(prices)
