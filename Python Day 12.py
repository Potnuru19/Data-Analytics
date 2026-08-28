'''
loops:
for statement:
A for loop is used to over a sequence or iterable datatypes
after for num is defined this variable at run to store values from ietrable datatypes
eg
nums = [12,3,5,78]
for num in nums:
    print(num)

else in for
unlike if-else, else block in for statement is executed fafter completed of all ietration
eg
nums = [12,3,5,78]
for num in nums:
    print(num)
else:
    print('for ended')

Break
the break used to stop iteration based on the condition given
eg
nums = [12,3,5,78]
for num in nums:
    print(num)
    if num == 3:
        break
eg
val_ = [1,2,3,4,5]
for j in val_:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd'}

Continue
the continue is keyword used to skip the current iteration based on the cpondition
eg
nums = [1,2,3,4,5,8,9]
for num in nums:
    if num == 5:
        continue
    print(num)

Pass
a pass is called as space holder, that is used after statement like (if,for,else)not to raise error
eg
for j in range(1,11):
    if j == 15:
        print(j)
    else:
        pass

assert
assert is a keyword used to check condition, incase the condition is false, it will raise the error(assertion error)
eg
age = 19
assert age>= 18
print('your eligible to vote')

While
num = 1
while num <= 5


'''

