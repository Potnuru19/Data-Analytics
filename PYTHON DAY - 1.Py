'''
PYTHON DAY - 1 *Introduction To Python*

What is a program?
Program is the process of instructions given by the user or programmer to planning what to do and how to do...
Eg:
user_en = 2000
bal_ = 10000
result = bal_ - user_en
print(result)

Procedural Language:
AN procedural language is organised mainly on functions.
Eg: C
def cal_ad(a,b):
   return a + b
a = 7
b = 9
any_ = cal_ad(a,b)
print(any_)

Object-oriented programming:
Object oriented programming is organised mainly on classes and object.
Eg: Python
num = 7
print(type(num))

What is python?
Python is:
High-level language: 
           Python take care about memory allocation.
           Eg: num = 9
               print(type(num))
               print(id(num))
    
Interpreter language:
            Line by line execution is followed by python that is the reason we call it as a interpreter language.
            Eg: num = 9
                num_2 = 90
                Print(num)
                print(type(num))
                print(id(num))

Dynamically typed language:
            No need to mention the type of data passing to the variable.
            Eg: num = 78
                any_ = ['Python']
                nums = [1,2]
                all_ = (1,2)
                print(type(num))
                print(type(any_))
                print(type(nums))
                print(type(all_))
Why python?
1. More libraries
2. Cross-platform
3. Open-source
4. simple syntax

Application:
Use in Data Science
Web Development
AI Artificial Intelligence
ML Machine Learning
DL Deep Learning

History Of Python:
It was started in early 1980's and released in the years 1991 by Guido Van Rossum.
And he pick the name from the most loved series called monty Python's circus.
The first version was released in the year 1991 which is python 0.9.0 and now the version we are using 3.14

Day 2

Tokens
Tokens are the small unit in the python..

1.Identifier
variable -->

num = 'Python'
print(type(num))

functions
def add_(a,b):
   print(a+b)

add_(4,5)

class
class details:
   pass

per_1 = details   

2.Keywords
Keywords are already saved in python for an specified reason to run..
eg
if
else
for
while
return
print

3.literals
Literals are  the datatypes that need to stored in variables...
num = 90
name = 'samitha'

4.operator
+ , - , = ,


statements
statements are the instructions given to the program...

num = 90
age = 2
if age >= 18:
    print(age)


comments
once comments are open the inside will never execute in python file

1.single line
2.multi-line  (''' ''', """ """)
used to comment more than one line

Variables
Bad ways
--> can't use number at 1st position
--> can't use special chat anywhere
--> can't use space
--> keywords
eg
2num = 90
$num= 90
n um = 78
if = 67

good ways 
--> small letters and cap letters, (_) underscores
eg
nUm_1 = 90
Num_2 = 78
samitha_rao = 90
eg
a = ('name':'samitha',
     'AC_num': '44567890987654')
b = ('name':'samitha',
    ('AC_num': '44567890987690')
c = ('name':'Rao',
     'AC_num': '44567890987678')

SBI_samitha_details = ('name':'samitha',
      'AC_num': '44567890987654')

ICICI_samitha_details = ('name':'samitha',
      'AC_num': '44567890987654')
num = 90
print(num)

num_3, num_2 = 56,89
print(num_3)
print(num_2)

swapping of two variables

a , b = 45,67
print('a=',a)
print('b=',b)
a, b = b, a
print('a=',a)
print('b=',b)

Day 3 Datatypes & TypeConversions
1.Numeric Datatype
  Float and integer is called as numeric datatype

Float
A number which contains decimal values, we call it as a float datatype
eg
56.89
price = 56.89

integer (int)
A normal number without any decimal values
eg
num = 89
num_2 = 6

2.String
String is a sequence of char that are enclosed in '',"",""""""
String is immutable
eg
any_ = 'Python is a language'
all_ = 'Ab,.&[)-+'

3.List
List is a collection of different datatypes
and it is represented by [] that are separated by ,
inside the list we call it as items
list is mutable
eg
any_ = [1,'Python',[5,6]]
print(type(any_))

4.Tuple
tuple is collection of different datatypes that are enclose in () and those are separated by ,
tuple is immutable
eg
nums = (1,89.67, 'Python',[3,4].(8,9))

5.Dictionary
Dictionary is collection of key:value pairs , keys and values are separated by :
key and value pair is call it as a item
and this items are separated by ,
Dictionary is represent using {}
in  key place we can use immutable datatypes
in values place we can use any datatype
eg
data_ = {1:2,
         'name':'Teja',
         (2,3):'Tuple'}
print(data_)

6.Set
set is collection unique elements and set can't allow any duplicate values inside it.....
set is represented by {} and the elements are separated by ,
an = {1,2,3}
print(an)

Type Conversion

float --> int, str
eg --> int
price = 45.78
print(int(price))

--> str()
price = 45.78
con = str(price)
print(type(con))

integer --> float, str
eg --> float()
num = 78
print(float(num))

--> str()
num = 78
con_ = str(num)
print(type(con_))

string --> int, float
eg --> int()
do = '3456'
print(int(do))

-->float()
do = '10.89'
print(float(do))

list --> tuple, string
eg --> tuple()
nums = [1,2,3,4]
print(tuple(nums))

eg
tuple --> list
eg --> list()
all_ = (5,6,7)
print(list(all_))

set --> tuple, list
eg --> tuple()
all_ = {5,6,7}
print(tuple(all_))

dictionary --> list
eg --> dict()

details = [('name','samitha'),('edu','Mca')]
print(dict(details))

Day 4

*** Concatination
The + will behave two ways for numerics it works normally and for other datatypes like string, list, tuple it concatinates

Operators
The opearators are used to perform operations in variables and the values.
1.Arithematic Operator
+, -, *, / , // , %
+ --> to add the values
num = 90
num_2 = 7
print(num + num_2)

- sub
a = 9
b = 7
print(a - b)

* multiplication
v = 8
n = 4
print(v * n)

/ division
v = 8
n = 4
print(v / n)

// floor divison
n = 8.6
n = 4.7
print(v // n)

2.Assignment Operator
=, +=, -=, *=, %=, /=

+= --> is increment operator
a = 0
print(a)
a += 1
print(a)

-= -->  decrement operator
b = 7
b -= 5
print(b)

*=
c = 7
c *= 2
print(c)

%=
d = 7
d %= 2
print(d)

/=
e = 5
e /= 7
print(e)

3.Comaprison Operator
==, >=, <=, >, < ,!=

==
num = 9
num_2 = 5
print(num == num_2)# 9 == 5

!=
num = 9
num_2 = 5
print(num != num_2)#9 != 5

>
num = 9
num_2 = 5
print(num > num_2)#9 > 5

<
num = 9
num_2 = 5
print(num < num_2)#9 < 5

>=
num = 10
num_2 = 9
print(num >= num_2)

<=
num = 10
num_2 = 9
print(num <= num_2)

4.Logical Operator
and --> both values should be true then the output is true, if one is false then the output is false
num = 9
num_2 = 13
print(num >= num_2 and num <= 10)# 9 >= 13 and 9 <= 10
print(num <= num_2 and num <= 10)# 9 <= 13 and 9 <= 10

or --> left or right is true then the output is true
num = 9
num_2 = 13
print(num >= num_2 or num < 10)

not --> gives the opposite output
num = 9
num_2 = 13
print(not(num >= num_2 or num < 10))

5.Identity Operator
is --> it checks the only outer values , it will not check the values which is inside the brackets
locations (object) checking
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
print(a is b)

is not --> gives the opposite output od is
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
print(a is not b)

6.Membership Operator
in --> particular variable is there in that datatype or not
nums = 'python is a language'
print('y' in nums)

not in --> condition satisfy
nums = 'python is a language'
print('i' not in nums)

7.Bitwise Operator


'''
num = 9
num_2 = 9
print(num == num_2)# 9 == 9





