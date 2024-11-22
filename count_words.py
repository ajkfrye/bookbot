def main():
    with open('books/frankenstein.txt') as f:
        text = f.read()
        split = text.split()
        word_count = 0
        for word in split:
            word_count += 1
    print(f'word count: {word_count}')
main()
