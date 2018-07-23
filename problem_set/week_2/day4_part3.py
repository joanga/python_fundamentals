#Part_1 of the excersie

# list_1 = input('Enter a set of numbers separated by commas: ').split(',')
# list_2 = input('Enter a second set of number separated by commas: ').split(',')
#
#
# list_1_set = set(list_1)
# list_2_set = set(list_2)
#
# common_num = list_1_set.intersection(list_2_set)
#
# print (common_num)

#PART #2
# word_list = input('Enter a set of words separated by commas: ').split(',')
#
# unique_words = set(word_list)
#
# print(unique_words)


#Part 3

vocabulary = set()
user_input = 0
while user_input != 'q':
    if user_input != 'v':
        input_word = input("Enter a word to add to vocabulary: ")
        if input_word != 'v':
            vocabulary.add(input_word)
            user_input = input_word
        else:
            user_input = input_word

    elif input_word == 'v':
        print (' '.join(vocabulary))

        input_word = input("Enter a word to add to vocabulary: ")
        vocabulary.add(input_word)
        user_input = input_word
