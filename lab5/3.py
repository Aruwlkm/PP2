import re
text = "my_variable another_One test_case someThing"
result = re.findall(r'[a-z]+_[a-z]+', text)
print(result)