'''Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.'''



thisbook={
  "Author":"Self",
  "Title":"Pyrhon All You Need",
  "Date Of Publish":2024
}

print(thisbook)



thislife={
"blessed":"By Allah",
"Who Take Cares All the Affairs":"Allah",
"Why we were created on this earth":"To Worship Allah and do good deeds"


}

print(thislife['blessed'])
print(len(thislife))
#checking the dictionary length

#indictionary items there can be different data types

thisis={
 
 "name":"jhon",
 "age":25,
 "city":True,
"colours":["red","green","yellow","blue","purple"]


}

print(thisis)
print(type(thisis))

'''Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

Example
Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)'''


#dict() Constructor :


thisishihi=dict(name="John",company="Google",address="Bangladesh")

print(thisishihi)