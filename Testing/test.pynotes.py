# Sorting items

# 1st Way
my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
print(my_list)

# Swap the 15 and 14 values
temp = my_list[2]
my_list[2] = my_list[0]
my_list[0] = temp

print(my_list)

# 2nd Way
my_list[0], my_list[2] = my_list[2], my_list[0]


# 15 57 14 33 72 79 26 56 42 40
# How can we sort this list by swapping numbers?

# Start
# 15 57 14 33 72 79 26 56 42 40

# 14 is smallest, swap 14 to pos 0
# 14 57 15 33 72 79 26 56 42 40

# 15 is next smallest, swap 15 to pos 1
# 14 15 57 33 72 79 26 56 42 40

# 26 is next smallest, swap with position 2
# 14 15 26 33 72 79 57 56 42 40

# 33 is the next smallest, swap with pos 3
# 14 15 26 33 72 79 57 56 42 40

# This is the SELECTION sort. I am SELECTING the smallest number and swapping.


def selection_sort(my_list): # best case, worst case = the same
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        # Swap
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)): # 100
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value): # worst - 50, average 25
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_value


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)

# Selection sort, all cases, best or worst
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1000, 1000 * 500 = 500,000
# n * (n / 2) = n^2 / 2

# Insertion sort, worst case
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1000, 1000 * 500 = 500,000
# n * (n / 2) = n^2 / 2

# Insertion sort, average case
# n = 10, 10 * 2.5 = 25
# n = 100, 100 * 14 = 2,500
# n = 1000, 1000 * 250 = 250,000
# n * (n / 4) = n^2 / 4

# Insertion sort, best case
# n = 10, 10 * 1 = 10
# n = 100, 100 * 1 = 100
# n = 1000, 1000 * 1 = 1,000
# n

# Insertion = more complicated, faster
# Selection = easier to use, slower

