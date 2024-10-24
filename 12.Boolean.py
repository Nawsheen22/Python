#In python we need to know a statement is true or false known as boolean
#output will show true or false
print(10>9)
print(10==9)
print(10<0)
#Message based on true or false 

a=100
b=300
if (a>b):
    print("a is greater than b")
else:
    print("b is greater than a")

    print(bool("Hello"))#true as not empty
    print(bool(15))#true as not empty

print(bool(""))        # Empty string
print(bool(0))         # Zero
print(bool([]))        # Empty list
print(bool(()))        # Empty tuple
print(bool({}))        # Empty dictionary
print(bool(None))      # None value
print(bool(False))     # False itself



class myclass():
  def __len__(self):
    return 0  #as returns 0 it will be false 

myobj = myclass()
print(bool(myobj))



def myFunction() :
  return True

print(myFunction()) # as returns true will be true


def myFunction() :
  return True

if myFunction():  #As the statement found that the function is true  it will executed and print yes
  print("YES!")
else:
  print("NO!")

#if a object is an integer or not 
x = 200
print(isinstance(x, int))