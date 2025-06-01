import sys
from stats import get_num_words, get_num_chars, sort_num_chars

def get_book_text(filepath: str) -> str:
    """Read the contents of a text file and return it as a string."""
    with open(filepath) as f:
        return f.read()

def print_report(book_path: str, word_count: int, sorted_char_count: list[dict[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    # Ensure book path when running script
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_count = get_num_chars(text)
    sorted_char_count = sort_num_chars(char_count)
    print_report(book_path, word_count, sorted_char_count)

if __name__ == "__main__":
    main()