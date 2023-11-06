book_path = "./books/frankenstein.txt"


def main():
    text = open_books(book_path)
    count = num_words(text)
    letters = count_letters(text)
    list_letters = sorted(
        list(letters.items()), key=lambda letter: letter[1], reverse=True
    )
    # print(list_letters)
    # print(dict_to_sorted_list(letters))


def num_words(str):
    words = str.split()
    count = len(words)
    return count


def dict_to_sorted_list(dict):
    cute_tuple = list(dict.items())
    return sorted(cute_tuple, key=lambda letter: letter[1], reverse=True)


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
