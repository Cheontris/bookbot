from stats import get_text_word_count
from stats import get_character_count
from stats import dictionary_sort
import sys
def main():
    if(not len(sys.argv) == 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_string = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_string}")
    with open(book_string) as f:
        print("----------- Word Count ----------")
        get_text_word_count(f.read())
    with open(book_string) as f:
        sort = dictionary_sort(get_character_count(f.read()))
        print ("--------- Character Count -------")
        for pair in sort:
            if pair["char"].isalpha():
                print(f"{pair["char"]}: {pair["num"]}")
        print("============= END ===============")
def get_book_text(file):
    print (file.read())

main()