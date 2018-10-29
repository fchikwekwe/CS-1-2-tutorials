"""
importing histogram_maker to use get_source_text and unique_words functions
"""
import histogram_maker

def dict_histogram(source_text):
    # takes in source text and returns a histogram in the form of a dictionary
    histogram = {} # empty dict to store histogram
    # checks each word in the source text
    for word in source_text:
        # lists that will go inside of histogram list
        count_and_word = []
        # counts up the words in the source text and adds count and word to list
        word_count = source_text.count(word)
        # using word as key since it is unique
        histogram[word] = word_count
        # removes all occurances of the word we've counted from original text
        while word in source_text:
            source_text.remove(word)
    # returns a dictionary
    return histogram

def frequency(word, histogram):
    # counts up the number of times that a word appears
    frequency_counter = 0
    # iterate over the histogram tuple
    for key, value in histogram.items():
        # check if the key is the same as the word parameter
        if key == word:
            # if it is, then increment the frequency_counter by the value
            frequency_counter += value
        else:
            pass
    return frequency_counter

if __name__ in '__main__':
    source_text = histogram_maker.get_source_text("souls_of_black_folk.txt")
    dict_histogram = dict_histogram(source_text)
    unique_words = histogram_maker.unique_words(dict_histogram)
    frequency = frequency("black", dict_histogram)
    print(frequency)

    f = open("histogram_logger.txt", "a")
    f.write("\n\nData Structure Type: Dictionary\nHistogram: {}\nNumber of Unique Words: {}\nFrequency of the word 'Veil': {}".format(dict_histogram, unique_words, frequency))
