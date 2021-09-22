# 'for Loop' -when you know how many times to loop
# 'while loop' -

repetitions = int(input("How  many times?"))

for i in range(repetitions):
    print("I will not chew gum in class.")

def print_about_gum(repetitions):
    for i in range (repetitions):
        print("I will not chew gum in class.")

for i in range(10):
    print(i)

name = "paul"
if name.lower() == "Paul":
    print("Yes")
else:
    print("No")

name= "mary"
if name.lower() == "bob" or "sam":
    print("Yes")
else:
    print("No")

if "10" < "2":
    print("Yes")
else: print("No")

if 10 < 2:
    print("Yes")
else:
    print("No")

if 3 =="3":
    print("Yes")
else:
    print("No")

if "3" == "3":
    print("Yes")
else:
    print("No")

a = 3 == 3
print(a)

a = 3 < 4
print(a)

def a(x):
    x = x + 1
    return x
x = 10
a(x)

print(x)

# Running total

total = 0
for i in range(5):
    new_number = int(input("Enter a number: "))
    total = total + new_number

print("The total is", total)

for i in range(5):
    print("Hello")

print("there.")

for i in range(10):
    print(i)

i=0
while i < 10:
    print(i)
    i += 1


# QUick review:
# Write a function called count_up that takes in two numbers.
# Prints all numbers from start to finish inclusive.
# Test with 5, 10

def count_up(start, end):

    for cur_number in range(start, end + 1):
        print(cur_number)

count_up(5, 10)

import random

my_number = random.randrange(50)
print(my_number)

for i in range(20):
    my_number = random.randrange(5)
    print(my_number)

for i in range(20):

my_number = random.randrange(5)
if my_number == 0:
    print("Dragon!")
else:
    print("No dragon.")

my_number = random.random()
print(my_number * 9 + 1)