with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def word_count(file):
    word_count = file.split()
    print(len(word_count))

word_count(file_contents)
