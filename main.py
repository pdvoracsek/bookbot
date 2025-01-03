def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    total_chars = sum(num_chars.values())
    chars_sorted = sorted(num_chars.items(), key=lambda x: x[1], reverse=True)
    print(f"-- Begin report of {book_path} --")
    print(f"{num_words} words found in the document")
    print("")
    for char, count in chars_sorted:
        percentage = (count / total_chars) * 100
        print(f"The '{char}' character occurs {count} times, {percentage:.2f}% of total characters")
    print("-- End report --")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    characters = {}
    for char in text:
        if char.isalpha():
            if char.lower() in characters:
                characters[char.lower()] += 1
            else:
                characters[char.lower()] = 1
    return characters


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
