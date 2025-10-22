import string
for letter in string.ascii_uppercase:
    with open(letter+".txt","w")as f:
        f.write("this is file " + letter + ".txt")
print("files created")