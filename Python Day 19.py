'''
Day 19 04/09/26

List comprehension
--> List comprehension is the short form of syntax to create a list
syntax1: --> [expression loop condition]
syntax2: [expression condition else loop]

eg
old_ = [1,2,3,5]
new_ = [i for i in old_]
print(new_)

old_ = 'python'
new_ = [i for i in old_]
print(new_)

old_ = [1,2,3,4,5]
new_ = [i for i in old_ if i%2==0]
print(new_)

range = 1 so it will multip with 1,2,3,4,5 and 6 will not be included
eg
any_ = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any_)

Nested comprehension
--> using list comprehension generating list inside list
any_ = any_ = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any_)
eg
of = [1,2,3],[4,5,6],[7,8,9]
data_ = [num for i in of for num in i]
print(data_)
this is called nested comprehension(decoding the matrices)

Generator
--> A generator is aspecial function which generate one value at a time
eg
def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))
print(next(j))









'''
def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))
print(next(j))
