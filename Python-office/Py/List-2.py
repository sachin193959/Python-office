
#len():- Returns Length of an Object
#Link:- https://www.programiz.com/python-programming/methods/built-in/len

"""
-The len() function returns the number of items (length) in an object.
-The syntax of len() is:

#len(s)

-len() Parameters:-
s - a sequence (string, bytes, tuple, list, or range) or a collection (dictionary, set or frozen set)

-Return Value from len():-
The len() function returns the number of items of an object.

Failing to pass an argument or passing an invalid argument will raise a TypeError exception.

"""

#Example 1: How len() works with tuples, lists and range?

"""
testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))

#output:-

[] length is 0
[1, 2, 3] length is 3
(1, 2, 3) length is 3
Length of range(1, 10) is 9

"""

#Example 2: How len() works with strings and bytes?

"""
testString = ''
print('Length of', testString, 'is', len(testString))

testString = 'Python'
print('Length of', testString, 'is', len(testString))

# byte object
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))

testList = [1, 2, 3]

# converting to bytes object
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))

#Output:

Length of  is 0
Length of Python is 6
Length of b'Python' is 6
Length of b'\x01\x02\x03' is 3


"""

#Example 3: How len() works with dictionaries and sets?

"""

testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))


#Output:-

{1, 2, 3} length is 3
set() length is 0
{1: 'one', 2: 'two'} length is 2
{} length is 0
frozenset({1, 2}) length is 2

"""
"""
#Internally, len() calls object's __len__ method. You can think of len() as:

def len(s):
    return s.__len__()
So, you can assign custom length to the object (if necessary)

"""
#Example 4: How len() works for custom objects?


"""
class Session:
    def __init__(self, number=0):
        self.number = number

    def __len__(self):
        return self.number


# default length is 0
s1 = Session()
print(len(s1))

# giving custom length
s2 = Session(6)
print(len(s2))


#Output:

0
6

==============================================================================================================================================================

"""

#max():- returns largest element
#Link:- https://www.programiz.com/python-programming/methods/built-in/max

"""
-The max() method returns the largest element in an iterable or largest of two or more parameters.

-Differnt syntaxes of max() are:

max(iterable, *iterables[,key, default])
max(arg1, arg2, *args[, key])

-If you want to find the smallest element, use min() method.



-
"""

#Example 1: Find maximum among the given numbers

"""
# using max(arg1, arg2, *args)
print('Maximum is:', max(1, 3, 2, 5, 4))

# using max(iterable)
num = [1, 3, 2, 8, 5, 10, 6]
print('Maximum is:', max(num))


#Output:

Maximum is: 5
Maximum is: 10

"""

#Example 2: Find number whose sum of digits is largest using key function

"""

def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

# using max(arg1, arg2, *args, key)
print('Maximum is:', max(100, 321, 267, 59, 40, key=sumDigit))

# using max(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print('Maximum is:', max(num, key=sumDigit))

#output:-

Maximum is: 267
Maximum is: 821

-Here, each element in the passed argument (list or argument) is passed to the same function sumDigit().

-Based on the return value of the sumDigit(), i.e. sum of the digits, the largest is returned.

"""


#Example 3: Find list with maximum length using key function



"""

num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using max(iterable, *iterables, key)
print('Maximum is:', max(num, num1, num2, key=len))


#Output:-

Maximum is: [15, 300, 2700, 821]

In this program, each iterable num, num1 and num2 is passed to the built-in method len().

Based on the result, i.e. length of each list, the list with maximum length is returned.


######################################################################################################################################################
"""

#Min() - returns smallest element

"""

-The min() method returns the smallest element in an iterable or smallest of two or more parameters.


"""