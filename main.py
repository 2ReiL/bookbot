def get_book_text(path: str) -> str:
    """Returns the contents of a file at a given path as a string"""
    with open(path) as f:
        return f.read()

def get_word_count(text: str) -> int:
    """Returns the number of words in a given string"""
    words_in_text: list = text.split()
    return len(words_in_text)

def get_letter_count(text: str) -> dict:
    """Returns a dictionary, where the key is a letter and the value 
    is the number of times it is found in a given string"""
    text_lower: str = text.lower()
    letter_count: dict = {chr(i): 0 for i in range(97, 123)}
    for characters in text_lower:
        if characters in letter_count.keys():
            letter_count[characters] += 1
    return letter_count

def print_report(path: str) -> None:
    """Prints a report of the book in a given path"""
    text: str = get_book_text(path)
    word_count: int = get_word_count(text)
    letters: dict = get_letter_count(text)    
    print(f"\n--- Begin report of {path} ---\n"
          f"{word_count} words found in the document\n")
    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---") 

def main() -> None:
    path: str = "books/frankenstein.txt"
    print_report(path)

if __name__ == "__main__":
    main()