#A tuple is a collection which is ordered and unchangable
#tuples are written in the round bracket 

thistuple=("Apple","Berry","Cherry")
print(thistuple)

#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1]

'''Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:'''



thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


'''To determine how many items a tuple has, use the len() function:'''


her=(1,2,3,4,5,6,7,8,9)

print(len(her))


'''One item tuple, remember the comma:'''

#if my item is only one , still i need to use the comma , as using comma will define the tuple or will cosider it string



you_must_use_comma=("Sure",)

print(type(you_must_use_comma))


you_must_use_comma=("Sure")

print(type(you_must_use_comma))

#you can use different data types in a tuple


integer_type=(1,2,3,4,5,6,7,8,9)
String_type=("haha","hihi","huhuhu")
boolean_type=(True,False,False,True)

print(type(integer_type))
print(type(boolean_type))
print(type(String_type))

#A tuple can contain different data types:

#Example
#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#Example
#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)