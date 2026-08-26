'''
elif
elif statement is used to check more possible outcomes or more conditions
eg
a = 90
b = 780
c = 670
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


eg
num = 7
num_2 = 3
user_opt = int(input('Enter \n1.add \n2.sub \n3.mul \n4.pow: '))
if user_opt == 1:
    print(num + num_2)
elif user_opt == 2:
    print(num - num_2)
elif user_opt == 3:
    print(num * num_2)
else:
    print(num ** num_2)


nested if
if inside an if statement is called nested if
eg
app_details = {'Pin':1234}
import random
user_pass = int(input("Enter your app password: "))
otp = random.randint(1000, 9999)
if user_pass == app_details['Pin']:
    print('password is correct')
    print(otp)
    user_otp = int(input("Enter 4 digit OTP: "))

    if user_otp == otp:
        print('Welcome to the app')
    else:
        print('incorrect OTP')
else:
    print('password is incorrect')
    
even or odd
eg
a = int(input("Enter a number: "))
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

eg
marks_ = int(input("Enter your marks: "))
if marks_ >=90:
    print('A+')
elif marks_ >=80:
    print('A')
elif marks_ >=70:
    print('B+')
elif marks_ >=60:
    print('B')
elif marks_ >=50:
    print('C+')
elif marks_ >=40:
    print('C')
else:
    print('Fail')


'''

marks_ = int(input("Enter your marks: "))
if marks_ >=90:
    print('A+')
elif marks_ >=80:
    print('A')
elif marks_ >=70:
    print('B+')
elif marks_ >=60:
    print('B')
elif marks_ >=50:
    print('C+')
elif marks_ >=40:
    print('C')
else:
    print('Fail')




























