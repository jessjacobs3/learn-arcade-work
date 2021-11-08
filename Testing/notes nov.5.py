# How many elements would I have to check on average (100)
100 / 2 = 50
# Worst case:
100
# Best case:
1
# Not in list:
100

# Number of items in the list is n
# Average
n / 2

# Worst case:
n

# Best case:
1

# Not in list:
n

def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")


    # Create an empty list to store our names

    name_list = []


    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()


        # Add the name to the list

        name_list.append(line)


    my_file.close()


    print( "There were", len(name_list), "names in the file.")


print(name_list)
print("There were", len(name_list), "names in the file.")


# Linear search
key = "Octavia the Siren"

lower_bound = 0
upper_bound = len(name_list) - 1
found = False
while lower_bound <= upper_bound and not found:
    middle_position = (lower_bound + upper_bound) // 2


    if name_list[middle_position] < key:
        lower_bound = middle_position + 1
    elif name_list[middle_position] > key:
        upper_bound = middle_position - 1
    else:
        found = True

    if found:
        print("Found at position:", middle_position)

# Binary search



# Worst case, binary search

128

7

2^7 = 128
2^16 = 65536
2^? = 1024

log2 1024 = 10

# Worst case, binary search, in terms of n,

log2(n)

main()
