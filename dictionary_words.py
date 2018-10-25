import random
import sys
import time # needed to record performance time
import datetime # needed to record when trials are done

# importing built-in word list
words = open("/usr/share/dict/words", "r")
# making words into list
word_list = words.read().replace("\n", " ").split()

def make_a_sentence(number_of_words):
    # keep track of word count
    word_count = 0
    # list to hold selected words
    sentence = []
    # keep checking how many words we have
    while word_count < number_of_words:
        # pick a random word from lists
        new_word = random.choice(word_list)
        # add to list
        sentence.append(new_word)
        # increment word count
        word_count += 1
        # piece together our final words into a string
    return sentence

if __name__ in '__main__':
    # command line argument
    number_of_words = int(sys.argv[1])
    # logging program performance time to dictionary word logger file
    start_time = time.process_time()

    final_sentence = ' '.join(make_a_sentence(number_of_words))
    # voila!
    print("Your incoherent sentence of the day is:\n{}.".format(final_sentence.capitalize()))

    # unsure how to write program to optimize more for speed; seems speedy to me
    # disabled logging function until needed
    f = open("dictionary_words_logger.txt", "a")
    f.write("\n\nCurrent date and time: {} \nProgram ran in {} seconds.".format(datetime.datetime.now(), time.process_time() - start_time))
