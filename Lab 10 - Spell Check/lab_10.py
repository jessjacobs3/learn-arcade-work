import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    dictionary = open("dictionary.txt")
    dictionary_list = []

    # Loop through each line in the word like a list
    for word in dictionary:
        word = word.strip()
        dictionary_list.append(word)

    dictionary.close()

    # Linear Search
    print("--- Linear Search ---")
    alice_file = open("AliceInWonderLand200.txt")
    word_list = []

    # Go through each word in the Alice file and add it to the word list
    line_number = 0
    for line in alice_file:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            current_position = 0
            while current_position < len(dictionary_list) and dictionary_list[current_position] != word.upper():
                current_position += 1
            if current_position == len(dictionary_list):
                print(" Line ", line_number, " possible misspelled word: ", word)

    # Binary Search
    print("---Binary Search---")
    line_number = 0
    story = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("Line" , line_number, " possible misspelled word: ", word)





if __name__ == "__main__":
    main()
