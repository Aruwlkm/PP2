a = 33
b = 200
if b > a:
  print("b is greater than a") #b is greater than a

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #a and b are equal

a = 33
b = 200
if b > a:
  pass 
# SyntaxError
"""match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")