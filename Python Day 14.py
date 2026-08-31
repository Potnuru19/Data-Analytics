'''
ran_ = int(input('Enter a number: '))
for j in range(1,ran_+1):
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')

for finding only odd
ran_ = int(input('Enter a number: '))
for j in range(1,ran_+1):
    if j % 2 != 0:
        print(f'{j} is odd')
    
nums = [23,78,97,5]
for j in nums:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')

finding vowels if we give upper only give PYTHON uppercase letters, lowercase letters python
aeiou = lowercase output
AEIOU = uppercase output

words_ = input("Enter a word: ")
vowels != 'aeiouAEIOU'
count = 0
for i in words_:
    if i in vowels:
        count += 1
        print(f'{i} is vowel')
print(count)

finding consonants
words_ = input("Enter a word: ")
vowels = 'aeiouAEIOU'
count = 0
for i in words_:
    if i not in vowels:
        count += 1
        print(f'{i} is consonant')
print(count)

finding the digits which is not repeated
digits_ = [1,2,3,1,5,3]
empty_ = []
for i in digits_:
    if i not in empty_:
        empty_.append(i)
print(empty_)


finding duplicates in tuple
digits_ = (1,2,3,1,5,3)
for i in tuple(digits_):
    if digits_.count(i) >1 :
        print(f'{i} is a duplicate')
    
        


        
'''
words_ = ' python is a language '
con_ = words_.split(' ')
print(con_)

words_ = 'Python is a language'
for i in words_:
    if i == ' ':
        print(
    
        
