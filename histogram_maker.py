

def get_source_text(file_name):
    # import text file and clean it of all punctuation
    punctuations = """!@#$%^&*()_-+=[]{}\|;':",./<>?`~"""
    source = open(file_name, "r").read().replace("\n", "").split()
    print(source)
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
            else:
                pass
    print(source)
    # source.splitlines()
    # print(source)

# def histogram(source_text)

if __name__ in '__main__':
    # get_source_text("example.txt")
    get_source_text("souls_of_black_folk.txt")
