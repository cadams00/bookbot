from stats import get_num_words,get_book_text,char_count,sorted_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        raise SystemExit(1)
    path = sys.argv[1]
    #path = "~/programming/bootdotdev/bookbot/books/frankenstein.txt"
    #path = "books/frankenstein.txt"
    #print(get_book_text(path))
    book = get_book_text(path)
    num_words = get_num_words(book)
    cc = (char_count(book))
    s = (sorted_dict(cc))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in s:
        print(f"{entry["char"]}: {entry["num"]}")

main()