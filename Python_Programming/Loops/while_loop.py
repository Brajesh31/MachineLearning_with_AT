# while_loop.py

# Basic while loop
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# While loop with break
num = 10
while num > 0:
    print(num)
    if num == 5:
        break
    num -= 1

# While loop with continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")
