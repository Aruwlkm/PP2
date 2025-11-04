thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #apple
           #banana
           #cherry 

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 #  apple
            # banana
            # cherry

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) # ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) 
# the syntax
# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"] # ['banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in range(10)] # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = [x for x in range(10) if x < 5] # [0, 1, 2, 3, 4]
newlist = [x.upper() for x in fruits] #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# sort lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)  # [50, 65, 23, 82, 100]

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']
