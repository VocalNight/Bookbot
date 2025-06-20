from stats import count_words
from stats import count_letters
from stats import printMessage
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Error ocurred, please insert an argument for the book path you want to analyze. Like so: python bookbot.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    lines = count_words(book)
    letter_list = count_letters(book)
    printMessage(lines, letter_list)


main()
