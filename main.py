from stats import number_of_words, number_of_characters, sorted_numbers
import sys

def get_book_text():
    with open(sys.argv[1], "r") as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    #book_text = get_book_text()
    #print(book_text)
    print('============BOOKBOT============')
    print("Analyzing book found at books/frankenstein.txt...")
    print('-----------Word Count-----------')
    number_of_words_in_book = number_of_words(get_book_text())
    print(f'Found {number_of_words_in_book} total words')
    t_in_text = number_of_characters(get_book_text())
    print('-----------Character Count-----------')
    sorted_numbers(t_in_text)
    print("============END============")
    


main()