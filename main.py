def main():
    book_filepath = "books/frankenstein.txt"
    book_contents = book_read(book_filepath)
    split_book = list_of_words(book_contents)
    word_count = num_of_words(split_book)
    print(f"This book contains: {word_count} words.")

def book_read(book):
    with open(book) as f:
        contents = f.read()
    return contents

def list_of_words(words):
    return words.split()

def num_of_words(words):
    return len(words)

if __name__ == "__main__":
    main()