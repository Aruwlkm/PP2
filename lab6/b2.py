def arip(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    
    print(f"upper: {upper}")
    print(f"lower: {lower}")
text = input()
arip(text)