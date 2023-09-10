# declaring and initializing arrays in python
my_list = []

#initializing a list with values
my_list = [1,2,3,4,5]

#initializing a list with mixed data types
mix_list = [1, "Hello", True, 3.14]



#=================================================================

#           ACCESSING ELEMENTS

#==================================================================

# Python uses "0" based indexing which means the first element of the
# list has an index of "0"

my_list = [10, 20, 30, 40, 50]

'''
Accessing the first element of the list
'''
first_element = my_list[0]  # Output is 10

'''
Accessing the second element of the list
'''
second_element = my_list[1] # Output is 20

'''
Accessing the last element of the list
'''
last_element = my_list[-1] # Output is 50

'''
Accessing the second_last element of the list
'''

second_last_element = my_list[-2] # Output is 40

# NEGATIVE INDEXES ARE USED TO COUNT ELEMENTS FROM THE END OF THE LIST



#=====================================================================

#             COMMON OPERATIONS

#=====================================================================


'''
Appending Elements

'''

my_list = [2,3,4,5,6]

my_list.append(4) # it appendes element to the end of the list

#Output is [2,3,4,5,6,4]


'''
Extending Arrays - used when you want to add multiple elements  to a list

'''

my_list = [2,3,4,5,6]

my_list.extend(['a','b']) #output is [2,3,4,5,6,'a','b']

my_list.extend([4,5, 6 ]) # output is [2,3,4,5,6,'a','b',4,5,6])

'''
Inserting Elements - Insert elements at specified positions in an array

'''
my_list = [1,4,6,7]
my_list.insert(1,5)  # insert 5 at index 1
# output is [1,4,6,7,4,5]  

'''
Deleting Elements - Removing elements from an array

'''

my_list = [1,4,6,7]
list.remove(1) # remove element by value(removes one)
list.pop(2) # remove element by index (removes element at index 2)
del my_list[3]     # Delete element by index (delete element at index 3)

#-----------------------------------------------------------------
#              KEY DIFFERENCE BETWEEN pop() AND del()
#----------------------------------------------------------------

# pop() method not only removes element at index but it also returns
# the removed element.
# del() is a python statement used to delete elements
#  in this context it remove an elemet at the index without
# returning it.


'''
Slicing Elements - extacts a subset of elements from an existing list

'''

my_list = [1,2,3,4,5,6]

sliced_list = my_list[1:4]

'''
Length of an Element - Find the number of elements in a list using the len() function.

'''

my_list = [1, 2, 3, 4]
length = len(my_list)

'''
Checking for Existence of an Element in the list

'''
my_list = [1, 2, 3]
exists = 3 in my_list

'''


'''