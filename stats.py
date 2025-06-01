def get_num_words(text: str) -> int:
    """Return the number of words in the given text."""
    return len(text.split())

def get_num_chars(text: str) -> dict:
    """Return a dictionary with lowercase character counts from the given text."""
    char_count = {}
    for char in text:
        char_lower = char.lower()
        char_count[char_lower] = char_count.get(char_lower, 0) + 1
    return char_count

def sort_num_chars(chars: dict[str, int]) -> list[dict[str, int]]:
    """Return a list of {'char': ..., 'num': ...} dicts sorted by count descending."""
    char_list = [{'char': key, 'num': value} for key, value in chars.items()]
    char_list.sort(key=lambda item: item['num'], reverse=True)
    return char_list