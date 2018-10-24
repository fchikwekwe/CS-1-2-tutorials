import sys
import random

# import dictionary of most English words
all_words = open("words.txt", "r")
# convert into list of strings without new line
word_list = all_words.read().replace("\n", " ").split()
# take our command line parameter and convert into list
original_word = list(sys.argv[1])

# v0 -- just reshuffles letter in word
# def anagram_gen(letters):
#     random.shuffle(letters)
#     new_word = ''.join(letters)
#     print(new_word)

# v1 -- check if the result is an actual word against list of most English words
def anagram_gen(search_word, all_words):
    # using loop to make sure that we are rechecking if word does not qualify
    making_word = True
    while making_word:
        # shuffle it up
        random.shuffle(search_word)
        # form the list back into a string
        new_word = "".join(search_word)
        # check against imported dictionary
        if new_word not in all_words:
            continue
        # success condition
        else:
            break
    # reform original word back into string
    first_word = "".join(original_word)
    # voila!
    print("An anagram of '{}' is '{}'.".format(first_word, new_word))


if __name__ in '__main__':
    anagram_gen(original_word, word_list)
