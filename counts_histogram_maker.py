"""
importing histogram_maker to use get_source_text and unique_words functions
"""
import histogram_maker

def counts_histogram(source_text):
    # takes in source text and returns a histogram in the form of a list of lists
    initial_histogram = [] # empty list to store histogram
    # checks each word in the source text
    for word in source_text:
        # lists that will go inside of histogram list
        count_and_word = []
        # counts up the words in the source text and adds count and word to list
        word_count = source_text.count(word)
        count_and_word.append(word_count)
        count_and_word.append(word)
        # then adds the smaller list to the histogram list
        initial_histogram.append(count_and_word)
    # removes duplicates from initial_histogram and adds to new histogram list
    print(initial_histogram)
    no_duplicates = [] # empty list to store unduplicated lists
    for list in initial_histogram:
        if list not in no_duplicates:
            no_duplicates.append(list)
        else:
            pass
    histogram = []
    print(no_duplicates)
    # check the zero index of each list in no_duplicates
    for list in no_duplicates:
    # compare that zero index to the zero indices of all lists in histogram
    # if there is no match, the append the entire list
    # if there is a match, then add the first index of that list to the matching list



if __name__ in '__main__':
    source_text = histogram_maker.get_source_text("souls_of_black_folk.txt")
    counts_histogram = counts_histogram(source_text)
    # print(counts_histogram)
