#What is String in Python?
"""
-A string is a sequence of characters.

-Strings can be created by enclosing characters inside a single quote or double quotes. Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

-Python String
In Python, Strings are arrays of bytes representing Unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

-Strings in Python can be created using single quotes or double quotes or even triple quotes.

-String in single quotes cannot hold any other single quoted character in it otherwise an error arises because the compiler won’t recognize where to start and end the string. To overcome this error, use of double quotes is preferred, because it helps in creation of Strings with single quotes in them. For strings which contain Double quoted words in them, use of triple quotes is suggested. Along with this, triple quotes also allow the creation of multiline strings.


"""

#Example:-

#Python String capitalize()	:-Converts first character to Capital Letter
"""
#In Python, the capitalize() method converts first character of a string to uppercase letter and lowercases all other characters, if any.

-The syntax of capitalize() is:

string.capitalize()

"""
#Example:-

s="my name is sachin"

print(s.capitalize())

#O/p:- My name is sachin #Here first word is capital.

#Example 2: Non-alphabetic First Character

string = "+ is an operator."

print(string.capitalize())       #For non-alphabetic it will give same output

#o/p:- + is an operator.

#############################################################################################################################################

#Python String center()	:-Pads string with specified character
"""
Using this we can able to give a space from the start of the string.

-The syntax of center() method is:

     string.center(width[, "fillchar"])

"""
#Example 1: center() Method With Default fillchar

string = "Python is awesome"

print(string.center(34))

print(string.center(34,"*"))  #Here * is print on both side

#o/p:-         Python is awesome
#op:- ********Python is awesome*********

#####################################################################################################################################################

#Python String count()
"""
-The string count() method returns the number of occurrences of a substring in the given string.

-In simple words, count() method searches the substring in the given string and returns how many times the substring is present in it.

-It also takes optional parameters start and end to specify the starting and ending positions in the string respectively.

-The syntax of count() method is:

         string.count(substring, start=..., end=...)

-substring - string whose count is to be found.
-start (Optional) - starting index within the string where search starts.
-end (Optional) - ending index within the string where search ends.

"""

#Example:-

S="Mobisoft infotech pvt ltd"

print(S.count("i"))

#o/p:- 2

print(S.count("i",4,12))  #start to count i word from 4th index and end at 12 th index

#o/p:- 1

####################################################################################################################################

#Python String find()
"""
-The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
-The syntax of find() method is:

   str.find(sub[, start[, end]] )

-find() Parameters
The find() method takes maximum of three parameters:

sub - It's the substring to be searched in the str string.
start and end (optional) - substring is searched within str[start:end]

Return Value from find()
The find() method returns an integer value.

If substring exists inside the string, it returns the index of first occurence of the substring.
If substring doesn't exist inside the string, it returns -1.

"""

#Example:-

X="Mobisoft infotech ltd"

print(X.find("ltd"))

#o/p:-18

#Example 2: rfind() With start and end Arguments

print(X.find("in",2,12))

#o/p:- 9

print(X.find("pvt"))   #Here pvt not in our string so its given by default value -1

#o/p:- -1

##############################################################################################################

#Python String index():- Returns Index of Substring
"""
-The index() method returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.
-The syntax of index() method for string is:

    str.index(sub[, start[, end]] )
-The index() method is similar to find() method for strings.

The only difference is that find() method returns -1 if the substring is not found, whereas index() throws an exception.

"""

#Example:-

w="Mobisoft infotech pvt ltd"

print(w.index("ltd"))

#o/p= 22

print(w.index("d"))

#o/p:- 24

#################################################################################################################

#Python String isalpha(): It all character is alphbetic or not
"""
-The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.
-The syntax of isalpha() is:

       string.isalpha()
-True if all characters in the string are alphabets (can be both lowercase and uppercase).
-False if at least one character is not alphabet.

"""
#Example:

x="Mobisoft"

print(x.isalnum())

#o/p:-True

y="3DPLM"

print(y.isalpha())

#o/p:-False


########################################################################################################################

#Python String isalnum(): it will check wether string conatains alphabete and numeric value if contains then it will give true otherwise it will give false.
"""
-The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
-The syntax of isalnum() is:

  string.isalnum()

- If white space contain between two word it will give false even there is alphanumric value.
"""

#Example:-
name = "M234onica"
print(name.isalnum())

#o/p:- True

# contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

#o/p: false  #false becoze there is white space between two words

name = "Mo3nicaGell22er"
print(name.isalnum())

#0/p:- True

name = "133"
print(name.isalnum())

#o/p:- True

########################################################################################################################

#Python String swapcase(): It is uesed to swapp upper latter to lower and visversa.
"""
-The string swapcase() method converts all uppercase characters to lowercase and all lowercase characters to uppercase characters of the given string, and returns it.
-The format of swapcase() method is:

   string.swapcase()
-
"""

#Example:-

t="ATPOST DIST Solapur TAL akkalakot"

print(t.swapcase())

#o/p:- atpost dist sOLAPUR tal AKKALAKOT

############################################################################################################################

#Python String partition(): Returns a Tuple

"""
-The partition() method splits the string at the first occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.
-The syntax of partition() is:

   string.partition(separator)
-
"""

#Example:-

p="I love my india"

print(p.partition("my"))

#o/p:- ('I love ', 'my', ' india')


#If word not present in string

print(p.partition("not"))

#o/p:- ('I love my india', '', '')

string = "Python is fun, isn't it"

print(string.partition("is"))

#o/p:- ('Python ', 'is', " fun, isn't it")

#####################################################################################################################

#Python String rpartition():- Returns a Tuple  #It will start from right side.
"""
-Python String rpartition()
The rpartition() splits the string at the last occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.

-The syntax of rpartition() is:

    string.rpartition(separator)

-
"""

#Example:-

string = "Python is fun"

print(string.rpartition("is"))

#o/p: ('Python ', 'is', ' fun')


print(string.rpartition('not '))

#o/p:- ('', '', 'Python is fun')



#Example2:-

string = "Python is fun, isn't it"

print(string.rpartition("is"))

#op:- ('Python is fun, ', 'is', "n't it")

##########################################################################################################################

#Python String replace(): -Replaces Substring Inside
"""
-The replace() method returns a copy of the string where all occurrences of a substring is replaced with another substring.
-The syntax of replace() is:

    str.replace(old, new [, count])

-The replace() method can take maximum of 3 parameters:

old - old substring you want to replace
new - new substring which would replace the old substring
count (optional) - the number of times you want to replace the old substring with the new substring

-
"""
#Example:-

string="Hello Everyone"

print(string.replace("Hello","Hi"))

#o/p:-Hi Everyone

print(string.replace("Hello","Hi",0))  #If you mentioned 0 here it will not replace any value it will print as it is.

#o/p:- Hello Everyone


#########################################################################################################################################################

#Python String split():- (Splits String from Left) Convert string to list
"""
-The split() method breaks up a string at the specified separator and returns a list of strings.
-The syntax of split() is:

   str.split([separator [, maxsplit]])

-split() Parameters
The split() method takes maximum of 2 parameters:

-separator (optional)- The is a delimiter. The string splits at the specified separator.
If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
-maxsplit (optional) - The maxsplit defines the maximum number of splits.
The default value of maxsplit is -1, meaning, no limit on the number of splits.

"""

#Example;-

k="Big fan of MSD"

print(k.split())

#o/p:- ['Big', 'fan', 'of', 'MSD']

k1="Big,fan:of*MSD"

print(k1.split(","))

#o/p:- ['Big', 'fan:of*MSD']


#Example:-

grocery = 'Milk, Chicken, Bread, Butter'

print(grocery.split(', ', 2))

#o/p:- ['Milk', 'Chicken', 'Bread, Butter']

#######################################################################################################################


#Python String rsplit():- Splits String From Right
"""
Python String rsplit()
-The rsplit() method splits string from the right at the specified separator and returns a list of strings.

-The syntax of rsplit() is:

str.rsplit([separator [, maxsplit]])
"""


#########################################################################################################################

#