# Multiline String
Nawsheen = """Currently Nawsheen Salsabeel a BSC in Computer Science is trying her
level best to learn python in a way, she can solve all the algorithms and learn Machine learning 
more faster. I mean it is not that bad to gain knowledge on things that make you happy.
Suddenly I have noticed that I am having super fun coding every day. Hey, coding is fun in Python.
I think Python is my favorite language now. I am having so much fun in Python. It seems easy, and I really
wanna do something good with this language. So here my long string ends! Hasta la vista!"""
print(Nawsheen)

# Strings are arrays in Python
Set = "Set Fire To The Rain"

# Printing the index element in the string
print(Set[4])  # Should print 'F'

# Looping through a string
for x in "banana":
    print(x)

# Looping through "Salsabeel" separately
for p in "Salsabeel":
    print(p)

# String length
Rule = '''When I was younger, I thought I would rule the world'''
print(len(Rule))  # Checking the length of the string (total number of characters)
#Check String 
CheckString="I am checking in this string if I can find the word Haha." 
print ("Haha" in CheckString) #They Answer with true or false.
                            #Here in is a keyword

#Now we will learn the if Statement to check the String 

FunBox="I really want to make an App for Palestine.An app where they will know from which foundation they are getting donated.And donation links.And there need"
if "Palestine" in FunBox:
   print("I am a Pro-Palestinian")

   #No string is found 

   Palestine="Jerusalem is the capital of Palestine"
   if "BULLSHIT Israel ,Terrorist" not in Palestine:
    print("BULLSHIT Israel DOEST NOT EXIST.")


#Slicing the String

SliceDlice="Hello!LifeZHereZ  going well" #only 'Here' will get printed
print(SliceDlice[10:15])

#Slice from Start

SliceDlice="Hello!Life Here  going well" #only 'Here' will get printed
print(SliceDlice[:19])

#Slice from a index to end


SliceDlice="Hello!Life Here  going well" #only 'Here' will get printed
print(SliceDlice[2:])

#Negative indexing that takes place end and -1 and eliminates the 1st index.

b = "Hello, World!"
print(b[-5:-2])





