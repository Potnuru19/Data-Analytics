'''
Day 18 03/09/26

Lambda function
lambda function is small anonymous function
lambda can take n number arguments, but only with one expression
the function is defined by using lambda keyword
syntax --> lambda arguments : expression (the exp[ressions should be single not multiple) 
eg
add_ = lambda a,b,c : a+b+c
print(add_(10,20,9))

even or odd
even = lambda num : num % 2 == 0
print(even(7))

greater or lesser
great_ = lambda a,b : a if a>b else b
print(great_(100,20))
    
cube value for any number using lambda function
cube = lambda a : a ** 3
print(cube(5))

filter
filter() function will perform only on selected elements of iterables
syntax --> filter(lambda arguments: expression, ietrable)
eg
nums = [1,2,3,4,5]
data_ = filter(lambda a: a%2==0,nums)
print(list(data_))

based on the condition, it gives the output
nums = [1,2,3,4,5]
data_ = filter(lambda a: a>2,nums)
print(list(data_))

map() condition gives the output on every value
map() function will perform on all elements of a ietrable
syntax --> 
nums = [1,2,3,4,5]
get_ = map(lambda a: a+6,nums)
print(list(get_))

filter() condition takes which is divisible and gives the output(numbers)
nums = [1,2,3,4,5]
get_ = filter(lambda a: a%2 == 0,nums)
print(list(get_))

reduce() is adding and gives the one value
the reduce() function repeatedly applies a function to the elements and reduces
them to one final value
it is available in the functools module
syntax --> reduce(lambda arguments: expression, iterable)
eg
from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,nums)
print(data_)
output: 1+2+3+4+5 = 15

from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,range(1,10))
print(data_)
output: 1+2+3+4+5+6+7+8+9 = 45


'''
from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,range(1,10))
print(data_)








