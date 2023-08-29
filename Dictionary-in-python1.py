'''Dictionary ---Buit in data type in Python
Dictionary are mutable,unordered collections with elements
in the form of a Key:Value pairs that associated keys to values'''
#It is also called associative arrays or mappings or hashes.
#Note
'''Keys of a dictionary must be of immutable types
such as
Python String
a number
a Tuple
if you try to give a mutable type as key
python will give #unhashable type" error'''
#Creating Dictionary
'''
d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
'''
#example
MLB_team = {
'Colorado' : 'Rockies',
'Boston'   : 'Red Sox',
'Minnesota': 'Twins',
'Milwaukee': 'Brewers',
'Seattle'  : 'Mariners'
}
print(MLB_team)

#Empty dictinary
#By a={}
#By dictinary constructor a=dic()
#a={}
a=dict()
a['RollNO']=1
a['Name']="Teena"
print(a)
#i
employee=dict(name='john',salary=1000,age=24)
print(employee)
#2
employee=dict({'name':'john','salary':10000,'age':24})
print(employee)

