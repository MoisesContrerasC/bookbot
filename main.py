from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_list
from stats import get_book_text
from stats import get_print_format

path_to_file = "books/frankenstein.txt"

def main():
    book_text = get_book_text(path_to_file)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_list = get_sorted_list(character_count)

    
    get_print_format(path_to_file, word_count, sorted_list)
main()
