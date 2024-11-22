def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    
    num_of_words = word_count(text)
    #print(f'{num_of_words} words')
    
    char_counts = char_count(text)
    #print(char_dict)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count(text)} words found in the document\n')
    print(char_report(char_count(text)))
    print('--- End report ---')
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    list = text.split()
    count = 0
    for word in list:
        count += 1
    return count

def char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def char_report(chars):
    for char in chars:
        print(f"the '{char}' character was found {chars[char]} times")

main()
