#In python the def is defined as a function 

def thisismy_functions():
    print("Hi I am new to learn this function hehehehe")

thisismy_functions()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")




def nawsheen_salsabeel(zzz,nnn,mariano,crazy):
   print(f"This that okay{mariano} to be {nnn} sometimes {crazy} and {zzz} ")


nawsheen_salsabeel("lazy","pretty","bonita?","talented")


def numberofkids(*kids):
   
  print(f"The kids are : {kids[0]}")

numberofkids("ndj","djfn","jend","hewed")

#In this way argument orders is just fine:


def nawsheen(child5,child1,child):
 print("Name of her children:"+ child5)

nawsheen(child="khikhi",child1="Khitthi",child5="Mawwa") 


#throwing everything in a dictionary with ***
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#if you dont call function through naming,it will count defaylt 

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


'''The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.'''
def myfunction():
  pass

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)