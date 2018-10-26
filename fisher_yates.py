import random

def fisher_yates_shuffle(list):
    list_length = len(list)

    for item in range(len(list)):
        random_item = random.choice(list)
        first_item = item
        print("first item {}".format(first_item))
        item = random_item
        print("item {}".format(item))
        random_item = first_item
        print("random item {}".format(random_item))
        print(list)
    return list


if __name__ in '__main__':
    list = ["0", "1", "2", "3", "4", "5"]
    fisher_yates_shuffle(list)
