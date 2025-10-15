import re
text = "Hello there From ChatGPT Lab"
result = re.findall(r'[A-Z][a-z]+', text)
print(result)