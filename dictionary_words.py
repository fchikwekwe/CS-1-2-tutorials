import random
import sys

words = open("/usr/share/dict/words", "r")
word_list = words.read().replace("\n", " ").split()
# print(word_list)
number_of_words = int(sys.argv[1])
# print(number_of_words)

def make_a_sentence(number_of_words):
    word_count = 0
    sentence = []
    while word_count < number_of_words:
        new_word = random.choice(word_list)
        # print(new_word)
        sentence.append(new_word)
        word_count += 1
        # print(sentence)
        final_sentence = ' '.join(sentence)
    print("Your incoherent sentence of the day is:\n{}.".format(final_sentence.capitalize()))

make_a_sentence(number_of_words)
