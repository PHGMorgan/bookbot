def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = file_contents.split()
        print(f"This book contains: {len(word_count)} words.")

if __name__ == "__main__":
    main()