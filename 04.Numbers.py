""" Basic int,float,comples and their conversion """
Nawsheen=2
Kiki=2.45543
milk=1j


a=float(Nawsheen)
b=int(Kiki)
c=complex(Kiki)  #Python does not allow direct conversion from a complex number to an integer.

print(a,b,c)

print(type(a),type(b),type(c))



import random
print(random.randrange(1, 10)) #randomly will print any number it wants every time we run the code 
"""Explanation:
random: This module in Python contains various functions to generate random numbers.
        randrange(start, stop): This function generates a random number from the range [start, stop) (i.e., it includes the start value but excludes the stop value).
        In my example:
         random.randrange(1, 10) generates a random integer between 1 (inclusive) and 10 (exclusive).
         This means the random number will be one of the following: 1, 2, 3, 4, 5, 6, 7, 8, or 9.""" 
