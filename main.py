import sys 
from stats import get_num_of_words, get_character_count,get_sorted_character

def get_book_text(filepath):
    file_content = ""
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def print_report(book_path, num_of_words, num_of_characters):
    print("============ BOOKBOT ============")
    book_text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------") 
    num_of_words = get_num_of_words(book_text)
    print(f"Found {num_of_words } total words")
    print("--------- Character Count -------")
    num_of_characters = get_sorted_character(get_character_count(book_text))
    for item in num_of_characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path= sys.argv[1]
    book_text = get_book_text(book_path)
    num_of_words = get_num_of_words(book_text)
    num_of_characters = get_sorted_character(get_character_count(book_text))

    print_report(book_path, num_of_words, num_of_characters)
    sys.exit(0)

main()