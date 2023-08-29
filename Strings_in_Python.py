'''String is a sequence of characters,which is enclosed
between either single (' ')
or double quotes (" "), python treats
both single and double quotes same.'''
#creating Strings
print("creating Strings")
print("************************************************************************")
s="Computer Science"
print(s)
a='Rita Sharma'
print(a)
c='''Rajkumar Sharma
lives at Jaipur'''#It is used to create string with multiple lines.
print(c)
d="""Teena is a Badminton
Player at Jaipur"""
print(d)
#Access Strings elements by Indexing -One elements
#Access Strings elements by Slicing-Extract elements in groups
print("______________________________________________________________________")
print("Access Strings elements by Indexing -One elements")
print("Access Strings elements by Slicing-Extract elements in groups")
print("______________________________________________________________________")
print('s[0]=',s[0])
print('s[8]=',s[8])
print('s[8]=',s[15])
print('s[0:16:1]',s[0:16:1])
print('s[2:]',s[2:])
print('s[::-1]',s[::-1])
print('s[-1:-5:-1]',s[-1:-5:-1])
print("______________________________________________________________________")
#Type of string of s--It is class
print("Type of string of s--It is class")
print(type(s))
print("______________________________________________________________________")
#Strings Operators Replication* concatenation + Membership operator
print("Strings Operators")
print(".........................................................................")
print("strings Replication Operator* 1 operand is string & another one is number")
print('s*2',s*2)
print('2*s',2*s)
print(".........................................................................")

print("+ concatenation operator/both operand should be string")


print('s+Python Learning=','***'+''+s+' '+'python Learning'+'***')
print('u in s=','u' in s)
print('u in s=','u' not in s)
sub="help"
string='helpinghand'
sub2='HELP'
print(sub in string)
print(sub2 in string)
print(sub not in string)
print(sub2 not in string)
#print(dir(s))

#string functions
'''
len() Returns the length of the string r=len(a) will be 4
str.capitalize() To capitalize the string r=a.capitalize() will be “COMP”
str.title() Will return title case string
str.upper() Will return string in upper case r=a.upper() will be “COMP”
str.lower() Will return string in lower case r=a.upper() will be “comp”
str.count()
will return the total count of a given element in a string
r=a.count(‘o’) will be 1
str.find(sub)
To find the substring position(starts from 0 index)
r=a.find (‘m’) will be 
str.find(sub)
To find the substring position(starts from 0 index)
r=a.find (‘m’) will be 2
str.replace()
Return the string with replaced sub strings
r=b.replace(‘my’,’your’) will be ‘your comp
str.index() Returns index position of substring
r=a.index(‘om’) will be 1
str.isalnum()
String consists of only alphanumeric characters (no symbols)
r=a.isalnum() will return True
str.isalpha()
String consists of only alphabetic characters (no symbols)
str.islower() String’s alphabetic characters are all lower case
str.isnumeric() String consists of only numeric characters
str.isspace() String consists of only whitespace characters
str.istitle() String is in title case
str.isupper() String’s alphabetic characters are all upper case
str.lstrip(char) str.rstrip(char)
Returns a copy of the string with leading/trailing characters removed
b=‘**comp’; r=b.lstrin() will be ‘comp’
str.strip(char)
Removes specific character from leading and trailing position 
str.split() Returns list of strings as splitted
b=‘my comp’; r=b.split() will be [‘my’,‘comp’]
str.partition() Partition the string on first occurrence of substring 
b=‘my comp’; r=b.partition(‘co mp’) will be [‘my’,‘comp’]
'''
print("LENGTH of S=",len('Computer science'))
print('rajkumar'.capitalize())
print('upper'.upper())
print('lower'.lower())
print('computer science'.count("c"))
print('title'.title())
print('todays menu'.title())
print('computer Science'.find('m'))
print("computer Science".replace("computer","IT"))
print("Computer Science".split())
txt = "apple#banana#cherry#orange"
x = txt.split("#")
y=txt.split("#",1)
print(x)
print(y)


'''Search for the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"'''

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

'''https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/'''





 

