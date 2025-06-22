# loop_else.py

# For loop with else
for num in range(3):
    print(f"Number: {num}")
else:
    print("Loop completed without break")

# For loop with break and else
for num in range(5):
    if num == 3:
        print(f"Breaking at {num}")
        break
    print(f"Number: {num}")
else:
    print("This will not print because of the break")

# While loop with else
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
else:
    print("While loop completed")
