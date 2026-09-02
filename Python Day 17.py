'''
Day 17 02/09/26

Scope of variables
1.Local variable
A variable is define inside the function call it as local variable,
where the variable can only access within that function
eg
def display():
    name = 'Samitha'
    print(name)
display()

error raises for print(name) because it given outside
def display():
    name = 'Samitha'
    print(name)
display()
print(name)

2.Global variable
A variable that is defined outside the function call and
it can be access anywhere throughout program
eg
a = 90
print(a)
def display():
    print(a)
display()
print(a)

Global Keyword
Global is keyword used to reaccess new values to variable
that was already define outside the function call
eg
a = 90
print(a)
def display():
    global a
    a = 10
display()
print(a)

Passing by value
eg
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(109)

Passing by reference
eg
num = 7
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)

Recursive function
The function call itself until the base condition is met..
eg
def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(5))

'''
def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(5))
