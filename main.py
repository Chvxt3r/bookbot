from stats import *
 
def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
    return(book_contents)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

def main2():
    book_text = get_book_text("books/frankenstein.txt")
    wc = wordcount(book_text)
    cs = charstats(book_text)
    print(f"{wc} words found in the document")
    print(f"{cs}")
    
main2()
