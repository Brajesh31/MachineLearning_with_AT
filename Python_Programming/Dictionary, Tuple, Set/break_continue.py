# break_continue.py

# Break in for loop
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(f"i: {i}")

# Continue in for loop
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")
