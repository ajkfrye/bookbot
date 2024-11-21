def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    
    num_of_words = word_count(text)
    #print(f'{num_of_words} words')
    
    char_dict = char_count(text)
    print(char_dict)

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
    dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    lowercase = text.lower()
    for letter in lowercase:
        for key in dict:
            if letter == key:
                dict[key] += 1
    return dict
main()
