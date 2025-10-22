data=['banana','cherry','alma']
with open('fruits.txt','w')as f:
    for item in data:
        f.write(item+'\n')
print("list written to file")