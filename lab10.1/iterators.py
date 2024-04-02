# Iterators
# Collections are objects that allow us to keep track of many other objects at once. You've likely used a collection before, for instance a list or dictionary in Python is a collection, as is an ArrayList in Java, or an array in any number of other languages. Collections are handy - instead of passing around a lot of individual objects we just need to pass around one. The type of collection you choose to solve a problem is important, and part of learning how to be a good coder is learning when to use each. Sometimes though, you want to write code that will work on any type of collection. This can be a problem, as not all collections work the same way. For instance, let's say you have the following:

# languages = [ "Arabic", "Chinese", "English", "French", "German", "Spanish" ]

# number_coders = { 'Ada':1, 'C':5, 'C++':2, 'Fortran':0, 'Python':12, 'Ruby':1 }
# And you want to write an algorithm that will print each element and count the number of elements at once. Students often want to write code like the following:

# def print_and_count(collection):
# 	total = 0
# 	for i in range(len(collection)):
# 		print(collection[i])
# 		total = total + 1
# 	return total
# This code will work fine with the languages list, but will crash with the dictionary. It would also crash on an unordered set - a data structure for which no order is implied. A set's order can change as we insert new elements. Those of you who have been programming for a while may have wanted to code this properly - instead of using a for loop based on the size of our data we use a for-each loop:

# def print_and_count(collection):
# 	total = 0
# 	for i in collection:
# 		print(i)
# 		total = total + 1
# 	return total
# A for-each loop doesn't care if a collection has an index or not, it simply loops over every element in the collection. But how does it work? How can our loop communicate with any collection type, and just as important, how can we make a collection that would work with Python's standard for-each loop in this way? The answer is that all Python collections are programmed to adhere to a common standard. This standard mandates that any object that is iterable must provide an iterator - that is, an object that we can ask for the next element in our collection. In Python we do this by providing the following two methods:

# def __iter__()

# def __next__()
# The first function returns an iterator object (it can be the same object or a different one). The iterator is an object that has __next__() defined - the method that is called whenever an object using our iterator wants the next element. Here's an example that would iterate over the alphabet (capital letters only):

# class Caps:
# 	# Set our initial values
# 	def __init__(self):
# 		self.value = -1
# 	# Say which object will be our iterator
# 	# Here we are saying we will be our own
# 	# iterator.
# 	def __iter__(self):
# 		return self
# 	# Provide the behavior of the next() function
# 	def __next__(self):
# 		if self.value < 25:
# 			self.value = self.value + 1
# 			return chr(self.value + 65)
# 		else:
# 			raise StopIteration()
# We can create a new instance of Caps now, and iterate with our foreach loop:

# c = Caps()
# for i in c:
# 	print(i, end='')
# print()
# And we should see

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# As the output. The StopIteration() exception is raised whenever an iterator is finished iterating.

# Now this code isn't exactly a collection - we don't really hold on to any other objects. But, it does serve to illustrate how we can write iterator code.

# A More Concrete Example
# Let's see another example. This time let's create a new type of list - one that actually holds other data. But instead of recreating a list as they already exist in Python, let's make one that does something more interesting. Let's say it gives you a random element from the list each time, deleting the element after it returns it to you. We will call this our RandomList.

# import random

# class RandomList:
#     def __init__(self):
#         self.data = []
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if len(self.data) == 0:
#             raise StopIteration()
#         item = random.choice(self.data)
#         self.data.remove(item)
#         return item
#     def add(self, item):
#         self.data.append(item)
# Let's examine what we did here. First, we created a class called RandomList. Our constructor made a new regular list in which to store our data. Our __iter__ method said that we each instance of RandomList would be its own iterator (meaning it would provide its own __next method). In our __next__ we simply used the random.choice function built into Python to randomly select one element from our list. We remove that item, then return it.


# Lab
# Create a data structure called BackwardList. Store data in a list. The iterator should start at the back of the list, and each call to __next__ will return an element that gets one index value closer to the front. Don't remove items from the list when you return them. So if our list was [ 1, 2, 3, 4, 5], the result of printing all the elements in a for-each loop would be 5 4 3 2 1. Make an add(self, item) method that appends the given item to the end of the list. If an item is added while iterating, reset the iterator to the new last element. So, if our list was [1 2 3] and we printed 3 2 and then added a new element 4, the iterator would point to the new element and print 4 3 2 1 until completed. The complete output in this case woudl be 3 2 4 3 2 1.

# Create a data structure called ListThirds. Use a list to store data, and have an add method that appends an element to the end of the list. The iterator must return the first element, then every third element, wrapping around if it reaches the end (use the modulo operator). So, if there are 10 elements in your list, you would return the 1st, 4th, 7th, 10th, 3rd, 6th, 9th, 2nd, 5th, and 8th. Keep track of the number of elements you have returned, and stop iterating when you have returned the same number as your list size. Don't worry about resetting if data is added while iterating.

# Create a data structure called SuperStack. Use a deque in the constructor to store the information. You may need an additional attribute to store the current index. Both of these attributes should be private. Create an append function that adds directly to the top of the stack. In addition, write a function to peek at the the current data on top of the stack and another to remove from the top of the stack. Finally add a function check_append. This function should look at the top three values of the stack, and compare the average of those three values to that of the incoming value. If the value is greater than the average of those three values, insert it at the bottom of the stack instead of the top.




import random
from collections import deque

class BackwardList:
    def __init__(self):
        self.data = []
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < -len(self.data):
            raise StopIteration()
        item = self.data[self.index]
        self.index = self.index - 1
        return item
    def add(self, item):
        self.data.append(item)
        self.index = -1
        
class ListThirds:
    def __init__(self):
        self.data = []
        self.index = 0
        self.size = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.size == len(self.data):
            raise StopIteration()
        item = self.data[self.index]
        self.index = (self.index + 3) % len(self.data)
        self.size = self.size + 1
        return item
    def add(self, item):
        self.data.append(item)
        
class SuperStack:
    def __init__(self):
        self.data = deque()
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration()
        item = self.data[self.index]
        self.index = self.index + 1
        return item
    def append(self, item):
        self.data.append(item)
    def peek(self):
        return self.data[-1]
    def remove(self):
        return self.data.pop()
    def check_append(self, item):
        if len(self.data) < 3:
            self.data.appendleft(item)
            return
        if item > sum(list(self.data)[-3:]) / 3:
            self.data.appendleft(item)
        else:
            self.data.append(item)
            
# Test
# Create a BackwardList object, add the numbers 1, 2, 3, 4, and 5, and then print the elements in a for-each loop. The output should be 5 4 3 2 1.
# Create a ListThirds object, add the numbers 1 through 10, and then print the elements in a for-each loop. The output should be 1 4 7 10 3 6 9 2 5 8.
# Create a SuperStack object, add the numbers 1 through 10, and then print the elements in a for-each loop. The output should be 10 9 8 7 6 5 4 3 2 1.

bl = BackwardList()
bl.add(1)
bl.add(2)
bl.add(3)
bl.add(4)
bl.add(5)
for i in bl:
    print(i, end=' ')
print()

lt = ListThirds()
for i in range(1, 11):
    lt.add(i)
for i in lt:
    print(i, end=' ')
print()

ss = SuperStack()
for i in range(1, 11):
    ss.append(i)
for i in ss:
    print(i, end=' ')
    
print()

