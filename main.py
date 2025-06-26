import sys
from stats import count_words, count_characters, sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        num_words = count_words(get_book_text(sys.argv[1]))
        num_charac = count_characters(get_book_text(sys.argv[1]))
        sorted_list = sort_list(num_charac)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in sorted_list:
            if i["name"].isalpha() != True:
                pass
            else:
                print(f"{i["name"]}: {i["num"]}")
        print("============= END ===============")
main()