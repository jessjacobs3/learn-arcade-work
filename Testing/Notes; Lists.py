x = [10, 20]
print(x[0])

# Index; pointer 0, 1, 2, 3, 4 (position in row of numbers)
# -values = starts backwards on list
# [0] = 3, [3] = 7, [-1] = 2
x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x[4])

x[2] = 22
print(x)

x = 18
print(18)

x = []
print(x)

# Prints out how many numbers there are in a list of x
x = []
size = len(x)
print(size)

my_list = [3, 7, 3]

for item in my_list:
    print(item)

my_list = ["Knife", "Spoon", "Fork"]
for item in my_list:
    print(item)

my_list = [[2, 3], [6, 5]]
for item in my_list:
    print(item)

my_list = [2, 3, 6, 5, 8, 10]

for i in range(len(my_list)):
    print(my_list[i])

for item in my_list:
    print(item)

for index, value in enumerate(my_list):
    print("Item", index, "is", value)

my_list = [2, 3, 6, 5, 8, 10, 31]
print(my_list)

# Add a number at the end of a list
my_list.append(100)
print(my_list)

my_list = []

for i in range(5):
    user_input = int(input("Enter an integer:"))
    my_list.append(user_input)

print(my_list)

my_list = [0] * 100
print(my_list)

my_list = ["hey"] * 100
print(my_list)

my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

list_total = 0

for item in my_list:
    list_total += item

print(list_total)

my_list = [3, 4, 4]
print(my_list)
my_list[0] = 4
