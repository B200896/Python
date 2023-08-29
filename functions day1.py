'''
def add():
    a=int(input("Enter no."))
    b=int(input("Enter the no."))
    c=a+b
    print(c)

add()
def sub():
    a=int(input("Enter no."))
    b=int(input("Enter no."))
    c=a-b
    print(c)
sub()  
#function without Argument without return value
def add():
    a=int(input("Enter no."))
    b=int(input("Enter the no."))
    c=a+b
    return c
d=add()
print(d)
#function without Argument with return value

def add(x,y):
    c=x+y
    print(c)
def sub(x,y):
    c=x-y
    print(c)


x=int(input("Enter no."))
y=int(input("Enter no."))
add(x,y)
sub(x,y)
#function with argument without return value
'''
def add(x,y):
    c=x+y
    return c
def sub(x,y):
    c=x-y
    return c

x=int(input("Enter no."))
y=int(input("Enter no."))
f=add(x,y)
print(f)
d=sub(x,y)
print(d)
#function with argument and with return value
