import re
pattern = r'a.*b'
test_strings = ['ab', 'axb', 'a123b', 'a_b', 'ac']
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(s)