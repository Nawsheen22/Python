#Variables in python does not required to declared as type . They can identify the variable type when we assign value to it

"""A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords. ref :W3Schools"""


""" Python variables follows three cases 1.Camel Case : except for 1st letter all starts with capital
example : myVariableName="Nawsheen"
2.Pascal case: All letter capital 
example : MyVariableName="Salsabeel"
3.Snake case: Underscore to add words or letters 
exmaple: My_variable_name="Khi khi the cat" """



x,y,z="Orange",'Apple','Malta'
print(x,y,z)

x1=y1=z1="Nawsheen"
print(x1,y1,z1)
#pov you wanna extract fruits from the list and put in a variable
fruits = ["apple", "banana", "cherry","Llichi","Mango"]
x2, y2,t2,g2,r2 = fruits
print(x2)
print(y2)
print(t2)
print(g2)
print(r2)
print (x2+y2+t2)


#pov you  want vthe variable that is in the function as global variable

def my_function():
     global gigi
     gigi = "Nawsheen"
     print("python is" +gigi)

     my_function()

     print("python is" +gigi)#pov it belongs to global scope so it wont get print to this function
#pov to test global variable
xx = "awesome"

def myfunc():
  xx = "fantastic"
  print("Python is " + xx)

myfunc()#after function callign prints the function

print("Python is " + xx) #prints the global








_life=20

print(_life)
X=5
Y="Salsabeel"
Z='BD'
print(X)
print(Y)
print(Z)

#pov u want to specify the type of the variable,thn we do type casting

x=str(3)
y=int(45)
w=float(3)

print(x,y,w)

"""suppose you can not determine the type of the variable, in that case 
you can simply use the type function to determine """

guessme='b'  # pov in python single and double quotation does not matter , so you end up saying str to both 

guessme2="Nawsheen Salsabeel"

guessme3=678.989

guessme4=8767


print(type(guessme),type(guessme2),type(guessme3),type(guessme4))
#pov Variable names are case sensative 

a = 4
A= 78
A='Nam nam'
print(a,A,A)

#POV python prints the recent variable that has been declared 

