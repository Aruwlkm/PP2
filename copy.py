thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # ['apple', 'banana', 'cherry']
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) #['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  #['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)  

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# append()   Adds an element at the end of the list
# clear()    Removes all the elements from the list
# copy()     Returns a copy of the list
# extend()   Add the elements of a list to the current list
# insert()   Adds an element at the specified position
# remove()   Removes the item with the specified value
# pop()      Removes the element at the specified position
# index()    Returns the index of the first element
# count()    Returns the number of elements with the specified value
# reverse()  Reverses the order of the list
# sort()     Sorts the list
