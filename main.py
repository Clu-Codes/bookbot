def main():
    book_path = "./books/frankenstein.txt"
    text = open_books(book_path)
    count = num_words(text)
    letters = count_letters(text)
    print(f"There are {count} words in this document.")
    print(letters)


def num_words(str):
    words = str.split()
    count = len(words)
    return count


def open_books(path):
    with open(path) as f:
        return f.read()


def count_letters(str):
    l_decomp = {}

    for letter in str:
        if letter.isalpha():
            low_letter = letter.lower()
            try:
                l_decomp[low_letter] += 1
            except:
                l_decomp[low_letter] = 1
    return l_decomp


main()
