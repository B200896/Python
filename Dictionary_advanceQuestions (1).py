#a list containing some items
my_list = ['a','a','b','b','b','c']

#initialise an empty dict
freq_dict = {}

#iterate through the list
for item in my_list:
    print(item)
    #if item not present, create new key and set it's (default) value to 1, 
    #since we have seen only 1 occurance till now
    if item not in freq_dict:
        freq_dict[item]=1
    '''else:
        #increment the count of the item by 1
        freq_dict[item]+=1'''

#print results
print(freq_dict)
# {'a': 2, 'b': 3, 'c': 1}
valList = ['1', '2', '3']
# Iterating the elements in list
   for val in valList:
      for ele in range(int(val), int(val) + 2):
         myDict.setdefault(ele, []).append(val)
print(myDict)
