
"""
This file creates and stores histograms of a source text.
This is a preamble to a tweet generator assignment for CS 1.2.
"""

def get_source_text(file_name):
    # import text file and clean it of all punctuation
    punctuations = """!@#$%^&*()_-+=[]{}\|;':",./<>?`~"""
    source = open(file_name, "r").read().replace("\n", "").split()
    # print(source)
    # checking word for punctuation and removing it
    for word in source:
        for character in word:
            if character in punctuations:
                # print(word)
                word_index = source.index(word)
                source.pop(word_index)
                new_word = word.replace(character, "")
                source.insert(word_index, new_word)
                word = new_word
                continue
            else:
                pass
    return source


def histogram(source_text):
    # takes in source text and returns a histogram in the form of a list of lists
    histogram = [] # empty list to store histogram
    # checks each word in the source text
    for word in source_text:
        # lists that will go inside of histogram list
        count_and_word = []
        # counts up the words in the source text and adds count and word to list
        word_count = source_text.count(word)
        count_and_word.append(word_count)
        count_and_word.append(word)
        # then adds the smaller list to the histogram list
        histogram.append(count_and_word)
        # removes all occurances of the word we've counted from original text
        while word in source_text:
            source_text.remove(word)
    # returns a list of lists
    return histogram

def unique_words(histogram):
    # this function counts up the first occurance of all words
    unique_words_count = 0
    # iterate over the whole list
    for gram in histogram:
        # increment our unique_words_count
        unique_words_count += 1
    # return the count as an integer
    return unique_words_count

def frequency(word, histogram):
    # this list counts up the number of times that a word appears
    frequency_counter = 0
    # iterate over the histogram list
    for gram in histogram:
        # check if the first element is the same as the word parameter
        if gram[1] == word:
            # if it is, then increment the frequency_counter by the value of the zeroth element
            frequency_counter += gram[0]
        else:
            pass
    return frequency_counter

if __name__ in '__main__':
    source_text = get_source_text("souls_of_black_folk.txt")
    histogram = histogram(source_text)
    unique_words = unique_words(histogram)
    word_frequency_example = frequency("black", histogram)
