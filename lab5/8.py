import re
text = "SplitAtUpperCaseLetters"
result = re.split(r'(?=[A-Z])', text)
print(result)