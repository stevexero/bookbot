def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print_report(text)

    # char_count = add_char_to_dict(text)
    # print(char_count)
    
    # word_length = count_words(text)
    # print(word_length)


def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    word_length = count_words(text)
    print(f"{word_length} words found in the document\n")
    chars = add_char_to_dict(text)
    for char in chars:
        print(f"The \'{char}\' character was found {chars[char]} times")
    print("--- End report ---")


def add_char_to_dict(words):
    char_set = set()
    char_dict = {}
    
    for char in words:
        if char.isalpha():
            char_set.add(char.lower())
    
    sorted_chars = sorted(char_set)
    
    for char in sorted_chars:
        char_dict[char] = 0

    for char in words:
        for char2 in char_dict:
            if char == char2:
                char_dict[char2] += 1

    return char_dict


def get_book_text(path):
    with open(path) as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)

main()
