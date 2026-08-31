'''
day 15

words = 'madam'
empty_str = ''
for i in words:
    empty_str = i + empty_str
if empty_str == words:
    print(f"{words} is a palindrome")
else:
    print(f"{words} is not a palindrome")


words = input("Enter a word: ")
empty_str = ''
for i in words:
    empty_str = i + empty_str
    print(empty_str)
if empty_str == words:
    print(f"{words} is a palindrome")
else:
    print(f"{words} is not a palindrome")

finding amstrong
eg
153
1 power is 1 and 5 power 125 by adding a before power 1 + 125 = 126 and 3 power is 27 then by adding 126 + 27 = 153,
the answer is same at the last so the number is amstrong. 
eg
num = int(input("Enter a number: "))
length_ = len(str(num))
amstrong_ = 0
for i in str(num):
    amstrong_ = amstrong_ + int(i)**length_
    print(amstrong_)
if amstrong_ == num:
    print(f'{num} is Amstrong Number')
else:
    print(f'{num} is not Amstrong Number')

finding perfect number
6 factors 1,2,3 by adding these 3, 1+2+3=6 so 6 is a perfect number.
1+2+4+7+14 = 28
eg
num = int(input("Enter a number: "))
sum = 1
for i in range(1, num):
    if num % 1 == 1:
        sum = sum + 1
if num == num:
    print("Perfect Number")
else:
    print("Not a perfect Number")

or

num = 34
sum_ = 0
for i in range(1,num):
    if num % i == 0:
        sum_ += i
if sum_ == num:
    print(f'{num} is a Perfect Number')
else:
    print(f'{num} is Not a perfect Number')

fabonacci series
adding last two numbers
eg
num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,10):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end=' ')









    


'''
num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,1000):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end=' ')
