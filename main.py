with open("books/frankenstein.txt") as f:
    file_contents = f.read()

char_dict = {}

def word_count(file):
    word_count = file.split()
    print("")
    print(f"Word count: {len(word_count)}")
    print("")

def char_count(file):
    for i in file.lower():
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    sort_list = list(char_dict.items())
    newlist = sorted(sort_list, key=lambda d: d[1], reverse=True)
    print("")
    print("-" * 80)
    print("")
    
    for t in newlist:
        if t[0].isalpha():
            print(f"The '{t[0]}' character was found {t[1]} times")
    
    print("")
    print("-" * 80)


word_count(file_contents)
char_count(file_contents)
