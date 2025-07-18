from stats import get_text_word_count
def main():
    with open("./books/frankenstein.txt") as f:
        get_text_word_count(f.read())
def get_book_text(file):
    print (file.read())

main()