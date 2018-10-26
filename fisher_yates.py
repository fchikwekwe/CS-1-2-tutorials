import random

def fisher_yates_shuffle(list):
    # if there are items to shuffle
    for index in range(len(list)):
        # pick a random index
        random_index = random.randint(0, len(list)-1)
        # swap it with the current element
        list[index], list[random_index] = list[random_index], list[index]
    return list


if __name__ in '__main__':
    list = ["a", "b", "c", "d", "e", "f"]
    print(fisher_yates_shuffle(list))
