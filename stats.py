
def count_words(book):
    return len(book)

def count_letters(book):
    letters = {}
    for i in book:
        if i.lower() in letters:
            letters[i.lower()] += 1
        else:
            letters[i.lower()] = 1

    return letters
