import re
text = "Style taza KZO"
result = re.findall(r'[A-Z][a-z]+', text)
print(result)