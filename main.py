from stats import count_words, count_letters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] 
    book = get_book_text(book_path)
    num_words = count_words(book.split()) 
    letters = count_letters(book) 
    #print(f"{num_words} words found in the document")
    #print(letters)
    print("="*12 + " BOOKBOT " + "="*12)
    print(f"Analyzing book found at {book_path}...")
    print("-"*10 + " Word Count " + "-"*10)
    print(f"Found {num_words} total words")

    print("-"*7 + " Character Count " + "-"*7)
    for x in letters:
        print(f"{x}: {letters[x]}")

    print("="*12 + " END " + "="*12)

def get_book_text(book_path):
    with open(book_path) as f:
        file_content = f.read()
        return file_content

main()
