def get_text_word_count(book_text):
    word_count = len(book_text.split())
    print (f"Found {word_count} total words")
def get_character_count(book_text):
    chars = []
    counts = []
    char_counts = {}
    for c in range (len(book_text)):
        if book_text[c].lower() not in chars:
            chars.append(book_text[c].lower())
            counts.append(1)
        else:
            counts[chars.index(book_text[c].lower())] += 1
    #Testing Lists:
    #print (chars)
    #print (counts)
    for c in range (len(chars)):
        char_counts[chars[c]] = counts[c]
    return (char_counts)
def dictionary_sort(dictionary):
    sorted_dictionary = []
    for c, n in dictionary.items():
        sorted_dictionary.append({"char" : c , "num" : n})
    sorted_dictionary.sort(reverse=True, key=sort_on)
    return sorted_dictionary
def sort_on(items):
    return items["num"]