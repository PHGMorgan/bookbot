def main():
    book_filepath = "books/frankenstein.txt"
    full_book = book_read(book_filepath)
    word_total = split_function(full_book)
    letters_count = letter_counter(full_book)
    letters_sort = dict_sort(letters_count)
    word_count = dict_of_words(full_book)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_total} words found in this document \n")

    print(f"The top five most used words are: {word_count[0]}, {word_count[1]}, {word_count[2]}, {word_count[3]}, and {word_count[4]}. \n")

    print(f"the five least used words are: {word_count[len(word_count) - 5]}, {word_count[len(word_count) - 4]}, {word_count[len(word_count) - 3]}, {word_count[len(word_count) - 2]}, {word_count[len(word_count) - 1]}. \n")

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


def dict_of_words(book_as_string):
    list_of_book_words = book_as_string.split()
    words_dict = {}
    sorted_words_list = []
    final_word_list = []
    for f in list_of_book_words:
        words_dict[f] = words_dict.get(f, 0) + 1
    for word in words_dict:
        sorted_words_list.append({"word": word, "number": words_dict[word]})
    sorted_words_list.sort(key=sort_by_number, reverse=True)
    for w in sorted_words_list:
        final_word_list.append(w["word"])
    return final_word_list


if __name__ == "__main__":
    main()