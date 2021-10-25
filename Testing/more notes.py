# Creating a list of numbers from user input

# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop through each element in myArray
for item in my_list:
    item = item * 2

for i in range(len(my_list)):
    my_list[i] *= 2

# Print the result
print(my_list)


x = "0123456789"

print("x=", x)
print("x[0]=", x[0])
print("x[1]=", x[1])
print("x[4]=", x[4])
print("x[-1]=", x[-1])

print("x[:5]=", x[:5])
print("x[5:]=", x[5:])


a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b +c)
print(3 * a)
print((a * 2) + (b * 2))

for character in "This is a test.":
    print(character)

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number:"))
month = months[(n - 1) * 3:(n - 1) * 3 + 3]
print(month)


plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(c, end=" ")

plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c)
    x += 1
    c2 = chr(x)
    print(c2, end="")

print()
encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"

for c in encrypted_text:
    x = ord(c)
    x -= 1
    c2 = chr(x)
    print(c2, end="")

my_list = [4, 2, 56, 2, 0]

biggest_number = 0
for item in my_list:
    if item > biggest_number:
        biggest_number = item

print(biggest_number)

my_list[-4, -2, -56, -2, -30]
biggest_number = my_list[0]
for item in my_list:
    if item > biggest_number:
        biggest_number = item

print(biggest_number)

my_list[-4, -2, -56, 2, 30]

positive_outlook_list = []
for item in my_list:
    if item > 0:
        positive_outlook_list.append(item)

    print(positive_outlook_list)

""" class -- child class of arcade.Window
    on_mouse_motion
    set_mouse_visible
    on_mouse_press
    
keyboard: 
    need starting position
    need move speed
    need to stop when key released
    on_key_press
    on_key_release 
    
game controller
    

"""







