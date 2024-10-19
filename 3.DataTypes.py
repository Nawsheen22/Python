""" Here basically we will learn, how we can know what kind of data type the variable is """

Query1= "She is a tech girl" #String,in python "",'' consider string
Query2=20#integer
Query3=20.5#float
Query4=1j #complex like better to know the function too complex(real,imaginary)
Query5=["Apple","Banana","Pineapple"] #list. You can even extract each element from this list
Query6=("Car","Pink Jeep","Double Decker") #tuple is actually fixed elements inside the 1st bracket that cannot be changed
Query7=range(6) # it prints like 0,1,2,3,4,5
Query8={"Name":"Nawsheen Salsabeel","Age":"24"} #dict known as dictionary in python.Dictionaries are used to store data values in key:value pairs. and we will know more later on
Query9={"White","Pink","Purple","White","Green"}#A set is a collection which is unordered, unchangeable*, and unindexed.
Query10=frozenset({"apple","Banana","Cherry"}) 
"""An immutable version of a Python set object
                               is a frozen set. While parts of a set can be changed at any moment, elements of a frozen set don’t change after they’ve been created.
                                    As a result, frozen sets can be used as Dictionary keys or as elements of other sets."""
Query11=True
Query12=b"Salsabeel"  
"""When you work with a byte string, you get byte values instead of characters.83 is the ASCII value of S.
                                    97 is the ASCII value of a."""
Query13=bytearray(5)   
"""bytearray(5) creates a bytearray of length 5, initialized with zeroes.
                             A  bytearray is mutable, meaning you can modify its contents.
                               In this case, Query13[0] = 100 updates the first element to the byte representation of 100, which corresponds to the ASCII character 'd'."""

Query14=memoryview(bytes(5))  
"""# Creating a memoryview of a bytes object of length 5
Query14 = memoryview(bytes(5))

# Print the memoryview
print("Memoryview:", Query14)

# Access the memoryview's content
print("Memoryview content (as list):", Query14.tolist())

# Access individual bytes
print("First byte in memoryview:", Query14[0])


Memoryview: <memory at 0x7f7e1d8f0f40>
Memoryview content (as list): [0, 0, 0, 0, 0]
First byte in memoryview: 0 """



Query15=None #nonetype






print(type(Query1),type(Query2),type(Query3),type(Query4),type(Query5),type(Query6),type(Query7),type(Query8),type(Query9),type(Query10),type(Query11),type(Query12),type(Query13),type(Query14),)
