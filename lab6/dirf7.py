src=input("source file:")
dst=input()
with open(src, 'r')as f1,open(dst, 'w')as f2:
    f2.write(f1.read())
print("File copied")