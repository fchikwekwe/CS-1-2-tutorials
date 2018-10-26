import random

def fisher_yates_shuffle(list):
    # if there are items to shuffle
    for item in list:
        # pick a random element
        random_item = random.choice(list)
        # get the indices of those elements
        item_index = list.index(item)
        random_item_index = list.index(random_item)
        # swap it with the current element
        list[item_index], list[random_item_index] = list[random_item_index], list[item_index]
    return list


if __name__ in '__main__':
    list = ["a", "b", "c", "d", "e", "f"]
    print(fisher_yates_shuffle(list))
