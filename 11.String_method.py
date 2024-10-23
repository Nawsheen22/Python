# capitalize()
print("hello world".capitalize())  # Output: 'Hello world'

# casefold()
print("HELLO WORLD".casefold())  # Output: 'hello world'

# center()
print("hello".center(10))  # Output: '  hello   '

# count()
print("hello world".count("l"))  # Output: 3

# encode()
print("hello".encode())  # Output: b'hello'

# endswith()
print("hello world".endswith("world"))  # Output: True

# expandtabs()
print("H\te\tl\tl\to".expandtabs(4))  # Output: 'H   e   l   l   o'

# find()
print("hello world".find("world"))  # Output: 6

# format()
print("Hello, {}!".format("John"))  # Output: 'Hello, John!'

# format_map()
data = {'name': 'John'}
print("{name}".format_map(data))  # Output: 'John'

# index()
print("hello world".index("world"))  # Output: 6

# isalnum()
print("hello123".isalnum())  # Output: True

# isalpha()
print("hello".isalpha())  # Output: True

# isascii()
print("hello".isascii())  # Output: True

# isdecimal()
print("1234".isdecimal())  # Output: True

# isdigit()
print("1234".isdigit())  # Output: True

# isidentifier()
print("variable1".isidentifier())  # Output: True

# islower()
print("hello".islower())  # Output: True

# isnumeric()
print("12345".isnumeric())  # Output: True

# isprintable()
print("hello".isprintable())  # Output: True

# isspace()
print("   ".isspace())  # Output: True

# istitle()
print("Hello World".istitle())  # Output: True

# isupper()
print("HELLO".isupper())  # Output: True

# join()
print(",".join(["apple", "banana", "cherry"]))  # Output: 'apple,banana,cherry'

# ljust()
print("hello".ljust(10))  # Output: 'hello     '

# lower()
print("HELLO".lower())  # Output: 'hello'

# lstrip()
print("  hello".lstrip())  # Output: 'hello'

# maketrans() and translate()
trans = str.maketrans("abc", "123")
print("abc".translate(trans))  # Output: '123'

# partition()
print("hello world".partition(" "))  # Output: ('hello', ' ', 'world')

# replace()
print("hello world".replace("world", "Python"))  # Output: 'hello Python'

# rfind()
print("hello world world".rfind("world"))  # Output: 12

# rindex()
print("hello world world".rindex("world"))  # Output: 12

# rjust()
print("hello".rjust(10))  # Output: '     hello'

# rpartition()
print("hello world".rpartition(" "))  # Output: ('hello', ' ', 'world')

# rsplit()
print("apple,banana,cherry".rsplit(","))  # Output: ['apple', 'banana', 'cherry']

# rstrip()
print("hello   ".rstrip())  # Output: 'hello'

# split()
print("apple banana cherry".split())  # Output: ['apple', 'banana', 'cherry']

# splitlines()
print("hello\nworld".splitlines())  # Output: ['hello', 'world']

# startswith()
print("hello world".startswith("hello"))  # Output: True

# strip()
print("  hello  ".strip())  # Output: 'hello'

# swapcase()
print("Hello World".swapcase())  # Output: 'hELLO wORLD'

# title()
print("hello world".title())  # Output: 'Hello World'

# upper()
print("hello".upper())  # Output: 'HELLO'

# zfill()
print("42".zfill(5))  # Output: '00042'
