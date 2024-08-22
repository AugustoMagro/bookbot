
class Main:
    def __init__(self):
        book_path = "books/frankenstein.txt"
        book = Main.read(book_path)
        words = Main.count_words(book.split())
        letters = Main.count_letters(book)
        report = Main.report(letters)
        report.sort(reverse=True, key=Main.sort_on)
        
        print("-"*10 + " Begin report of " + book_path + "-"*10)
        print(f"{words} words found in the document")

        for x in report:
            print(f"The '{x["letter"]}' character was found {x["count"]} times")

        print("-"*10 + " End report " + "-"*10)

    def sort_on(dict):
        return dict["count"]

    def read(path):
        with open(path) as f:
            return f.read()

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

    def report(data):
        list_letters = []
        for x in data:
            if x.isalpha() == True:
                list_letters.append({"letter":x, "count":data[x]})
        return list_letters
        
Main()
