def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(f"---Begin report of {book_path}---")
    print(f"{get_num_words(text)} words found in the document\n")

    counter = get_chars_dict(text)
    sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)

    for [x, count] in sorted_counter:
        if 'a' <= x and x <= 'z':
            print(f"The '{x}' character was found {count} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(book):
    return len(book.split())

def get_chars_dict(book):
    chars = {}
    new_book = book.lower()
    for x in new_book:
        if x in chars:
            chars[x] += 1 
        else:
            chars[x] = 1
    return chars

main()
