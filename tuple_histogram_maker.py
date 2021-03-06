"""
importing histogram_maker to use get_source_text and unique_words functions
"""
import histogram_maker

def tuple_histogram(source_text):
    # takes in source text and returns a histogram in the form of a tuple
    initial_histogram = [] # empty list will change to tuple later
    histogram_index = 0 # keep track of index to use to add to tuple
    # checks each word in the source text
    for word in source_text:
        # lists that will go inside of histogram
        count_and_word = []
        # counts up the words in the source text and adds count and word to list
        word_count = source_text.count(word)
        count_and_word.append(word_count)
        count_and_word.append(word)
        # then adds the smaller list to the histogram list
        initial_histogram.append(count_and_word)
        # increments index number
        histogram_index += 1
        # removes all occurances of the word we've counted from original text
    histogram = []
    for list in initial_histogram:
        if list not in histogram:
            histogram.append(list)
        else:
            pass
    # returns a tuple
    return tuple(histogram)

def frequency(word, histogram):
    # counts up the number of times that a word appears
    frequency_counter = 0
    # iterate over the histogram tuple
    for count, tuple_word in histogram:
        # check if the first element is the same as the word parameter
        if tuple_word == word:
            # if it is, then increment the frequency_counter by the value of the zeroth element
            frequency_counter += count
        else:
            pass
    return frequency_counter

if __name__ in '__main__':
    source_text = histogram_maker.get_source_text("souls_of_black_folk.txt")
    tuple_histogram = tuple_histogram(source_text)
    unique_words = histogram_maker.unique_words(tuple_histogram)
    frequency = frequency("the", tuple_histogram)
    histogram_maker.logger("histogram_logger.txt", "Tuple", tuple_histogram, unique_words, "the", frequency)
