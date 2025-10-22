import time
num = int(input())
mils = int(input())
time.sleep(mils / 1000)
print("Square root of", num,  "after", mils, "milliseconds is", pow(num, 0.5))