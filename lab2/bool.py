print(10 > 9)  #true
print(10 == 9) #false
print(10 < 9)  #false

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")  #b is not greater than a
  

#The bool() function allows you to evaluate any value,
# and give you True or False in return,

print(bool("Hello"))  #true
print(bool(15))       #true

x = "Hello"
y = 15
print(bool(x))   #true
print(bool(y))   #true
print(bool("abc"))  #true
print(bool(123))    #true
print(bool(["apple", "cherry", "banana"]))  #true
print(bool(False)) #false
print(bool(None)) #false
print(bool(0)) #false
print(bool("")) #false
print(bool(())) #false
print(bool([])) #false
print(bool({})) #false

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) #false

def myFunction() :
  return True
print(myFunction()) #true
x = 200
print(isinstance(x, int)) #true
