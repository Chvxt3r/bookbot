from stats import *
 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    chars_dict = charstats(text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item['num']}")

    print("============= END ===============")


main()
