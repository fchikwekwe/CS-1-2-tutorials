import random

def random_word(histogram):
    # iterate over the histogram
    for word in histogram:
        # using random module to get a random items
        # used random.choice initially, but then changed to random.randint
        random_index = random.randrange(len(histogram))

    random_word = histogram[random_index]
    return random_word

def weighted_probablity(weighted_histogram):
    not_chosen = True
    # results = {}
    while not_chosen:
        random_choice = random.choice(weighted_histogram)
        word = random_choice[0]
        probability = random_choice[1]
        random_number = random.uniform(0,1)
        if probability > random_number:
            # print("failure")
            # print(random_choice, random_number)
            return word
            # if word not in results:
            #     results.update({word: 1})
            # else:
            #     results[word] += 1
            # return results
            not_chosen = False
        else:
            # print("success")
            # print(choice, random_number)
            continue

# if the word is not in the new array, then add it
# if the word is already in the new array, then increment frequency


if __name__ in '__main__':
    histogram = ["there", "once", "was", "a", "man", "from", "nantucket"]
    weighted_histogram = [["there", 0.1], ["once", 0.2], ["was", 0.1], ["a", 0.1], ["man", 0.1], ["from", 0.1], ["nantucket", 0.3]]
    # print("Your random histogram word is:\n{}".format(random_word(histogram)))
    for _ in range(10):
        print(weighted_probablity(weighted_histogram))
