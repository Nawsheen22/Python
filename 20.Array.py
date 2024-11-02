cars = ["Ford", "Volvo", "BMW"] #Created an Array
'''Accessing Array'''
# Creating an array (list) of integers
array = [10, 20, 30, 40, 50]
print("Array:", array)
print("First element:", array[0])    # Output: 10
print("Last element:", array[-1])    # Output: 50

'''Adding Element'''
array.append(60)      # Adds 60 to the end
array.insert(2, 25)   # Inserts 25 at index 2
print("Array after adding elements:", array)


'''Removing Elements'''
array.remove(25)       # Removes the first occurrence of 25
removed_element = array.pop(2)   # Removes element at index 2
print("Array after removing elements:", array)
print("Removed element:", removed_element)

'''Iterating Through Array'''
print("Elements in array:")
for element in array:
    print(element)

'''Finding an element in array'''
print("Elements in array:")
for element in array:
    print(element)

'''Sorting an Array'''
# Using sorted() returns a new sorted list
sorted_array = sorted(array)
print("Sorted array:", sorted_array)

# Using sort() sorts the list in place
array.sort()
print("Array sorted in place:", array)


'''Array Length'''

length = len(array)
print("Length of array:", length)

'''Sum and Average of Elements'''
total = sum(array)
average = total / len(array)
print("Sum of array:", total)
print("Average of array:", average)


'''Finding Minimum and Maximum'''
min_value = min(array)
max_value = max(array)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
