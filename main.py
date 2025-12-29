from stats import count_words, char_counts, sorted_char_counts
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # def get_book_text(path):
    #     with open(path) as file:
    #         contents = file.read()
    #     print(contents)

    # text_path = "books/frankenstein.txt"
    text_path = sys.argv[1]

    # get_book_text(text_path)
    # message = count_words(text_path)
    # char_counts(text_path)
    d = char_counts(text_path)
    l = sorted_char_counts(d)

    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {count_words(text_path)} total words
--------- Character Count -------""")
    for dict in l:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}\n")

    print("=================================")


if __name__ == "__main__":
    main()
