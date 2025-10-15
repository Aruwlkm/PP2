import re
text = "InsertSpacesBetweenWordsLikeThis"
result = re.sub(r'(?=[A-Z])', ' ', text).strip()
print(result)