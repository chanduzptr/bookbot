from stats import count_words, count_char, sorted_count_char
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    num_words = count_words(content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    count_char_result = count_char(content)
    sorted_list = sorted_count_char(count_char_result)
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")

main()