import random

def random_word(histogram):
    # iterate over the histogram
    for word in histogram:
        # using random module to get a random items
        # used random.choice initially, but then changed to random.randint
        random_index = random.randint(0, len(histogram)-1)

    random_word = histogram[random_index]
    return random_word

if __name__ in '__main__':
    histogram = ["there", "once", "was", "a", "man", "from", "nantucket"]
    print("Your random histogram word is:\n{}".format(random_word(histogram)))
