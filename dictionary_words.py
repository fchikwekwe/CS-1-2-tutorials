import random
import sys
import time # needed to record performance time
import datetime # needed to record when trials are done

def get_source_text(file):
    # importing built-in word list
    words = open(file, "r")
    # making words into list
    word_list = words.read().replace("\n", " ").split()
    return word_list

def get_random_words(number_of_words, word_list):
    # keep track of word count
    word_count = 0
    # list to hold selected words
    words_for_sentence = []
    # keep checking how many words we have
    while word_count < number_of_words:
        # pick a random word from lists
        new_word = random.choice(word_list)
        # add to list
        words_for_sentence.append(new_word)
        # increment word count
        word_count += 1
        # piece together our final words into a string
    return words_for_sentence

def make_a_sentence():
    pass

def logger(file):
    f = open(file, "a")
    f.write("\n\nCurrent date and time: {} \nProgram ran in {} seconds.".format(datetime.datetime.now(), time.process_time() - start_time))

if __name__ in '__main__':
    # command line argument
    number_of_words = int(sys.argv[1])
    # logging program performance time to dictionary word logger file
    start_time = time.process_time()
    word_list = get_source_text("/usr/share/dict/words")
    final_sentence = ' '.join(get_random_words(number_of_words, word_list))
    # voila!
    print("Your incoherent sentence of the day is:\n{}.".format(final_sentence.capitalize()))

    # unsure how to write program to optimize more for speed; seems speedy to me
    logger("dictionary_words_logger.txt")
