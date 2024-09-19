def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_filepath = "books/frankenstein.txt"
    full_book = book_read(book_filepath)
    word_count = split_function(full_book)
    letters_count = letter_counter(full_book)
    letters_sort = dict_sort(letters_count)   
    print(f"{word_count} words found in this document \n")
    for item in letters_sort:
        print(f"The '{item['letter']}' character was found {item['number']} times")
    print("--- End report ---")

def book_read(book):
    with open(book) as f:
        contents = f.read()
    return contents

def split_function(words):
    return len(words.split())

def letter_counter(book):
    letters_dict = {}
    for f in book:
        if f.isalpha() == True:
            lowercase = f.lower()
            letters_dict[lowercase] = letters_dict.get(lowercase, 0) + 1
    return letters_dict

def dict_sort(dictionary):
    dict_list = []
    for letter, number in dictionary.items():
        temp_dict = {}
        temp_dict["letter"] = letter
        temp_dict["number"] = number
        dict_list.append(temp_dict)
    dict_list.sort(key=sort_by_number, reverse=True)
    return dict_list

def sort_by_number(item):
    return item["number"]

if __name__ == "__main__":
    main()