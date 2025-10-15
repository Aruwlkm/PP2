import re
text = "Python, is great. Indeed it is"
result = re.sub(r'[ ,.]', ':', text)
print(result)