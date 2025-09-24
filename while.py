i = 1
while i < 6:
  print(i)
  i += 1
# 1 2 3 4 5

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 #   1 2 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # 1 2 4 5 6 
  # for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # apple banana cherry

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break # apple banana