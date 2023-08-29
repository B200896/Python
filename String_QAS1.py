#Q1 Programs that reads a line and prints its statistics like:
'''
Number of uppercase letters:
Number of lowercase letters
Number of alphabets
Number of digits
'''
#solution1

'''
line=input("Enter a line:")
lowercount=0
uppercount=0
digitcount=0
alphacount=0
for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    if a.isalpha():
        alphacount+=1
print("Number of uppercase letters:",uppercount)
print("Number of lowercaseletters:",lowercount)
print("Number of alphabets:",alphacount)
print("Number of digits:",digitcount)
'''

#Q2 Program that reads a line and a substring. It should then display the number
#of occurrences of the given substring in the line
#Soution2
#find(value,start,end)
'''
line=input("enter a line")
sub=input("enter a substring")
length=len(line)
print("string length",length)
lensub=len(sub)
print("lensub",lensub)
start=0
count=0
end=length
while True:
    print("****")
    pos=line.find(sub,start,end)
    print("position",pos)
    if pos!=-1:
        count+=1
        start=pos+lensub
        print("start=",start)
    else:
        print("bye bye")
        break
    

    if start>=length:
        print("bye")
        break
print("No. of occurrences of",sub,':',count)
'''

#Q3 Write a program that takes a string with multiple words
#and then capitalize the first letter of each word and
#forms a string out of it
#Solution3
string=input("enter string:")
length=len(string)
a=0
end=length
string2=''
while a<length:
    if a==0:
        string2+=string[0].upper()
        a+=1
    elif (string[a]=='' and string[a+1]!=''):
        string2+=string[a]+ string[a+1].upper()
        a+=2
    else:
        string2+=string[a]
        a+=1
print("original strings:",string)
print("capitalized words strings",string2)
'''
'''
#Q4Write a program that reads a string and check whether it is a pailndrome string or not.
string=input("Enter String:")
length=len(string)
print(length)
mid=length//2
print(mid)
rev=-1
flag=0
for a in range(mid):
    if string[a]==string[rev]:
        a+=1
        rev-=1        
    else:
        flag=1
        print("bye")
        break
if flag==1:
    print("string is not a pailindrome")
else:
    print("string is pailindrome")
'''
#https://www.geeksforgeeks.org/python-program-check-string-palindrome-not
#Q5 Write a program that reads a string and display the longest substring of the
#given string having just the consonants.
#https://www.geeksforgeeks.org/longest-subsequence-of-a-string-containing-only-consonants
#solution
'''
string=input("enter a string:")
length=len(string)
maxlength=0
maxsub=''
sub=' '
lensub=0
for a in range(length):
    if string[a] in 'aeiou' or string[a] in 'AEIOU':
        if lensub>maxlength:
            maxsub=sub
            maxlength=lensub
            sub=''
            lensub=0
    else:
        sub+=string[a]
        lensub=len(sub)
    a+=1
print("Maximum length consonant substring is:",maxsub,end='  ')
print("with",maxlength,"Charachter")
'''
#Q6 Write a program that reads a string and then prints a string that capitalizes every
#other letter in the string e.g., passion becomes pAsSiOn.
#solution
'''
string=input("enter a string:")
length=len(string)
print("originsl dtring:",string)
string2=" "
for a in range(0,length,2):
    string2+=string[a]
    if(a<(length-1)):
        string2+=string[a+1].upper()
print("Alternatively capitalized string:",string2)
'''
#Q7.Write a program that reads email-id of a person in the form
#of a string and ensures that it belongs to domain@edupillar.com.
#(Assumption:No invalid character are there in email-id)
#solution
email=input("enter your email id:")
domain='@edupillar.com'
ledo=len(domain)
print(ledo)
lema=len(email)
print(lema)
sub=email[lema-ledo:]
print("dssd",sub)
if sub==domain:
    if ledo!=lema:
        print("It is valid email id")
    else:
        print("This is invalid email id-contains just the domain name.")
else:
    print("this email-id is either not valid or belongs to some other domain.")

