myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # {'banana', 'cherry', 'apple'}
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # 3
set1 = {"abc", 34, True, 40, "male"}  #{True, 34, 40, 'male', 'abc'}

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # 'banana', 'cherry', 'orange', 'apple'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)  # {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

# remove , discard , pop, clear , del
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # {'cherry', 'apple'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #{3, 2, 'c', 'a', 1, 'b'}

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)  # {'banana', 'cherry'}
 # frozenset is an immutable version of a set.

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) # frozenset({'cherry', 'apple', 'banana'})
# <class 'frozenset'>
"""
copy()	 	Returns a shallow copy	
difference()	-	Returns a new frozenset with the difference	
intersection()	&	Returns a new frozenset with the intersection	
isdisjoint()	 	Returns whether two frozensets have an intersection	
issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union """