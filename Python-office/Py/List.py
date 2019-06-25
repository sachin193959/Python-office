#Append

#Example 1: Adding Element to a List

"""
animal = ['cat', 'dog', 'rabbit']
animal.append("man")                         #For string need "" or ''
print(animal)

animal = ['cat', 'dog', 'rabbit']
animal.append(2)                             #It added deirectory.
print(animal)

#Output:

['cat', 'dog', 'rabbit', 'man']
['cat', 'dog', 'rabbit', 2]

"""

#Example 2: Adding List to a List

"""
List1=[1,2,3,4,5,6,7]
List2=[8,9,10,11,12,13,14]

List1.append(List2)              #It will add list2 one data to list1
print(List1)

List2.append(List1)              #It will add list1 one data to list2
print(List2)

#Output:-

[1, 2, 3, 4, 5, 6, 7, [8, 9, 10, 11, 12, 13, 14]]
[8, 9, 10, 11, 12, 13, 14, [1, 2, 3, 4, 5, 6, 7, [...]]]

========================================================================================================================
"""

#Extend:- In list we have  not able to add muliple element at a time so to add multiple element we need to create another list and using extend we add in it.

#Example 1: Using extend() Method
"""
# language list
language = ['French', 'English', 'German']

# another list of language
language1 = ['Spanish', 'Portuguese']

language.extend(language1)

# Extended List
print('Language List: ', language)

#Output:

Language List:  ['French', 'English', 'German', 'Spanish', 'Portuguese']

"""

#Example 2: Add Elements of Tuple and Set to List

"""
# language list
language = ['French', 'English', 'German']   #This is a list.

# language tuple
language_tuple = ('Spanish', 'Portuguese')   #This is a tuple.

# language set
language_set = {'Chinese', 'Japanese'}        #This is a set.

#language.extend(list(language_tuple))    #Convert tuple to list

#OR

language.extend(language_tuple)

print('New Language List: ', language)


language.extend(list(language_set))        #Convert set to list

print('After tuple now list Language List: ', language)




#Output:-

New Language List:  ['French', 'English', 'German', 'Spanish', 'Portuguese']
After tuple now list Language List:  ['French', 'English', 'German', 'Spanish', 'Portuguese', 'Japanese', 'Chinese']

===============================================================================================================================================

"""

#Insert:-

#The insert() method inserts an element to the list at a given index.

#Example 1: Inserting Element to List

"""
# vowel list
vowel = ['a', 'e', 'i', 'u']

# inserting element to list at 4th position
vowel.insert(3, 'o')                               #Here 3 is index position and o is item to be added in that position.

print('Updated List: ', vowel)

#Output:-

Updated List:  ['a', 'e', 'i', 'o', 'u']

"""

#Example 2: Inserting a Tuple (as an Element) to the List

"""
#List
mixed_list = [{1, 2}, [5, 6, 7]]
#Here postion   0         1

# number tuple
number_tuple = (3, 4)

# inserting tuple to the list
mixed_list.insert(1, number_tuple)

print('Updated List: ', mixed_list)

#Output:

Updated List:  [{1, 2}, (3, 4), [5, 6, 7]]


#It is important to note that the index in Python starts from 0, not 1.

#If you have to insert an element at the 4th place, you have to pass 3 as an index. Similarly, if you have to insert an element at the 2nd place, you have to use 1 as an index.


================================================================================================================================================================

"""

#Remove:

#The remove() method searches for the given element in the list and removes the first matching element.

#The syntax of remove() method is:

#list.remove(element)

#Example 1: Remove Element From The List

"""
# animal list
animal = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' element is removed
animal.remove('rabbit')                              #Here "rabbit"  removed from list.

#Updated Animal List
print('Updated animal list: ', animal)

#Output:

Updated animal list:  ['cat', 'dog', 'guinea pig']

"""

#Example 2: remove() Method on a List having Duplicate Elements


# If a list contains duplicate elements
# the remove() method removes only the first instance

"""
# animal list
animal = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' element is removed
animal.remove('dog')                                 #There are two 'dogs' in list so Here, only the first occurrence of element dog is removed from the list.


#Updated Animal List
print('Updated animal list: ', animal)


#Output:

Updated animal list:  ['cat', 'dog', 'guinea pig']


"""

#Example 3: Trying to Delete Element That Doesn't Exist

"""

# animal list
animal = ['cat', 'dog', 'rabbit', 'guinea pig']

# Deleting 'fish' element
animal.remove('fish')

# Updated Animal List
print('Updated animal list: ', animal)

#Output:-

Traceback (most recent call last):
  File ".. .. ..", line 5, in <module>
    animal.remove('fish')
ValueError: list.remove(x): x not in list

========================================================================================================================================================

"""

#Index:- returns smallest index of element in list

#The index() method searches an element in the list and returns its index.

"""
In simple terms, index() method finds the given element in a list and returns its position.

However, if the same element is present more than once, index() method returns its smallest/first position.

Note: Index in Python starts from 0 not 1.

The syntax of index() method for list is:

#list.index(element)

"""

#Example 1: Find position of element in the list

"""
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# element 'e' is searched
index = vowels.index('e')

# index of 'e' is printed
print('The index of e:', index)

# element 'i' is searched
index = vowels.index('i')

# only the first index of the element is printed
print('The index of i:', index)


#Output:

The index of e: 1
The index of i: 2

"""

#Example 2: Index of element not present in the list

"""
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# element 'p' is searched
index = vowels.index('p')

# index is printed
print('The index of p:', index)

#Output:

Traceback (most recent call last):
  File "/home/midt-032/Videos/Py/List.py", line 273, in <module>
    index = vowels.index('p')
ValueError: 'p' is not in list

"""

#Example 3: Find index of tuple and list inside a list

"""
# random list
random = ['a', ('a', 'b'), [3, 4]]

# random list
random = ['a', ('a', 'b'), [3, 4]]

# element ('a', 'b') is searched
index = random.index(('a', 'b'))

# index is printed
print("The index of ('a', 'b'):", index)

# element [3, 4] is searched
index = random.index([3, 4])

# index is printed
print("The index of [3, 4]:", index)

#Output:

The index of ('a', 'b'): 1
The index of [3, 4]: 2

==========================================================================================================================================================

"""

#Count:- returns occurrences of element in a list
#Link:- https://www.programiz.com/python-programming/methods/list/count
"""
-The count() method returns the number of occurrences of an element in a list.

-In simple terms, count() method counts how many times an element has occurred in a list and returns it.

-The syntax of count() method is:

=>list.count(element)

#count() Parameters
-The count() method takes a single argument:
element - element whose count is to be found.

#Return value from count()
The count() method returns the number of occurrences of an element in a list.

"""

#Example 1: Count the occurrence of an element in the list

"""
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)


#Output:

The count of i is: 2
The count of p is: 0


"""

#Example 2: Count the occurrence of tuple and list inside the list

"""
# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)

#Output:

The count of ('a', 'b') is: 2
The count of [3, 4] is: 1

"""

#POP() :- Removes Element at Given Index

#Link:-  https://www.programiz.com/python-programming/methods/list/pop

"""
-The pop() method removes the item at the given index from the list. The method also returns the removed item.

-The syntax of the pop() method is:

#list.pop(index)

-pop() parameter:-

-The pop() method takes a single argument (index) and removes the item present at that index.

-If the index passed to the pop() method is not in range, it throws IndexError: pop index out of range exception.

-The parameter passed to the pop() method is optional. If no parameter is passed, the default index -1 is passed as an argument which returns the last item.

-Return Value from pop():-
-The pop() method returns the item present at the given index. This item will be removed the list.

"""

#Example 1: Print Element Present at the Given Index from the List

"""
#programming language list
language = ['Python', 'Java', 'C++', 'French', 'C']

# programming language list
language = ['Python', 'Java', 'C++', 'French', 'C']

# Return value from pop()
# When 3 is passed
return_value = language.pop(3)
print('Return Value: ', return_value)

# Updated List
print('Updated List: ', language)

#Output:

Return Value:  French
Updated List:  ['Python', 'Java', 'C++', 'C']

-It is important to note that the index in Python starts from 0, not 1.

-So, if you need to pop 4th element, you need to pass 3 to the pop() method.

"""

#Example 2: pop() without an index, and for negative indices

"""
# programming language list
language = ['Python', 'Java', 'C++', 'Ruby', 'C']

# When index is not passed
print('When index is not passed:')
print('Return Value: ', language.pop())
print('Updated List: ', language)

# When -1 is passed
# Pops Last Element
print('\nWhen -1 is passed:')
print('Return Value: ', language.pop(-1))
print('Updated List: ', language)

# When -3 is passed
# Pops Third Last Element
print('\nWhen -3 is passed:')
print('Return Value: ', language.pop(-3))
print('Updated List: ', language)

#Output:

When index is not passed:
Return Value:  C
Updated List:  ['Python', 'Java', 'C++', 'Ruby']

When -1 is passed:
Return Value:  Ruby
Updated List:  ['Python', 'Java', 'C++']

When -3 is passed:
Return Value:  Python
Updated List:  ['Java', 'C++']

=======================================================================================================================================================

"""
"""

Diff Between del,remove and pop.

Yes, remove removes the first matching value, not a specific index:

>>> a = [0, 2, 3, 2]
>>> a.remove(2)
>>> a
[0, 3, 2]
del removes the item at a specific index:

>>> a = [3, 2, 2, 1]
>>> del a[1]
>>> a
[3, 2, 1]
and pop removes the item at a specific index and returns it.

>>> a = [4, 3, 5]
>>> a.pop(1)
3
>>> a
[4, 5]
Their error modes are different too:

>>> a = [4, 5, 6]
>>> a.remove(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> del a[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> a.pop(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range

======================================================================================================================================================

"""

#reverse()- Reverses a List

#Link:- https://www.programiz.com/python-programming/methods/list/reverse

"""
-The reverse() method reverses the elements of a given list.

-The syntax of reverse() method is:

#list.reverse()

-reverse() parameter:-
The reverse() function doesn't take any argument.

-Return Value from reverse():-
The reverse() function doesn't return any value. It only reverses the elements and updates the list.

"""

#Example 1: Reverse a List

"""
# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)


#Output:

Original List: ['Windows', 'macOS', 'Linux']
Updated List: ['Linux', 'macOS', 'Windows']

"""

#Example 2: Reverse a List Using Slicing Operator

"""
# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# Reversing a list
#Syntax: reversed_list = os[start:stop:step]
reversed_list = os[::-1]

# updated list
print('Updated List:', reversed_list)

#Output:
Original List: ['Windows', 'macOS', 'Linux']
Updated List: ['Linux', 'macOS', 'Windows']

"""
#Example 3: Accessing Individual Elements in Reversed Order


"""

# Operating System List
os = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(os):
    print(o)

#Output:

Linux
macOS
Windows

======================================================================================================================================================

"""

#Sort():- sorts elements of a list

#Link:- https://www.programiz.com/python-programming/methods/list/sort

"""

-The sort() method sorts the elements of a given list.
-The sort() method sorts the elements of a given list in a specific order - Ascending or Descending.

-The syntax of sort() method is:

#list.sort(key=..., reverse=...)

-Alternatively, you can also use Python's in-built function sorted() for the same purpose.

#sorted(list, key=..., reverse=...)

-Note: Simplest difference between sort() and sorted() is: sort() doesn't return any value while, sorted() returns an iterable list.

-sort() Parameters:-

-By default, sort() doesn't require any extra parameters. However, it has two optional parameters:

-reverse - If true, the sorted list is reversed (or sorted in Descending order)
-key - function that serves as a key for the sort comparison

-Return value from sort()
sort() method doesn't return any value. Rather, it changes the original list.

If you want the original list, use sorted().


"""

#Example 1: Sort a given list


"""
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

#Output:

Sorted list: ['a', 'e', 'i', 'o', 'u']

"""

"""
-How to sort in Descending order?

sort() method accepts a reverse parameter as an optional argument.

-Setting reverse=True sorts the list in the descending order.

#list.sort(reverse=True)

-Alternately for sorted(), you can use the following code.

#sorted(list, reverse=True)
"""

#Example 2: Sort the list in Descending order

"""

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)

#Output:-

Sorted list (in Descending): ['u', 'o', 'i', 'e', 'a']

"""

"""
How to sort using your own function with key parameter?
If you want your own implementation for sorting, sort() also accepts a key function as an optional parameter.

Based on the results of the key function, you can sort the given list.

list.sort(key=len)
Alternatively for sorted

sorted(list, key=len)
Here, len is the Python's in-built function to count the length of an element.

The list is sorted based on the length of its each element, from lowest count to highest.
"""

#Example 3: Sort the list using key

"""
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)

#Output:

Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

===========================================================================================================================================================

"""
#Copy():- Returns Shallow Copy of a List
#Link:-https://www.programiz.com/python-programming/methods/list/copy

"""
-The copy() method returns a shallow copy of the list.

-A list can be copied with = operator. For example:

old_list = [1, 2, 3]
​new_list = old_list

-The problem with copying the list in this way is that if you modify the new_list, the old_list is also modified.

-However, if you need the original list unchanged when the new list is modified, you can use copy() method. This is called shallow copy.

-The syntax of copy() method is:

#new_list = list.copy()

"""


#Example of Both original and new file modified:

"""
old_list = [1, 2, 3]
new_list = old_list

# add element to list
new_list.append('a')

print('New List:', new_list )
print('Old List:', old_list )

#Output:

New List: [1, 2, 3, 'a']
Old List: [1, 2, 3, 'a']

"""

#Example of only new file modified:

"""
# mixed list
list = ['cat', 0, 6.7]

# copying a list
new_list = list.copy()

# Adding element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List: ', list)
print('New List: ', new_list)

#Output:

Old List:  ['cat', 0, 6.7]
New List:  ['cat', 0, 6.7, 'dog']

"""

#Example 2: Shallow Copy of a List Using Slicing

"""
# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List: ', list)
print('New List: ', new_list)

#Output:


Old List:  ['cat', 0, 6.7]
New List:  ['cat', 0, 6.7, 'dog']

==================================================================================================================================================
"""


#Clear()- Removes all Items from the List
#Link:- https://www.programiz.com/python-programming/methods/list/clear

"""
-The clear() method removes all items from the list.

-The syntax of clear() method is:

#list.clear()

-clear() Parameters:
The clear() method doesn't take any parameters.

-Return Value from clear():
The clear() method only empties the given list. It doesn't return any value.
"""

##Example 1: Working of clear() method

"""
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)

#Output:

List: []

"""

#Note: If you are using Python 2 or Python 3.2 and below, you cannot use the clear() method. You can use the del operator instead.

#Example 2: Emptying the List Using del..

"""
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list)

#Output:

List: []

=====================================================================================================================================================
"""



