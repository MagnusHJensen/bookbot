

def main():
    name = "books/frankenstein.txt"
    with open(name) as file:
        text = file.read()
        count = word_count(text)
        char_count = character_count(text)
        print_report(count, char_count, name)


def word_count(text: str) -> int:
    return len(text.split())

def character_count(text: str) -> int:
    counts = {}
    
    # Iterate over each character in the text
    for char in text:
        # Check if the character is lowercase
        if char.lower():
            # If the character is already in the dictionary, increment its count
            if char in counts:
                counts[char] += 1
            # Otherwise, add the character to the dictionary with a count of 1
            else:
                counts[char] = 1
    
    return counts

def print_report(word_count: int, character_count: dict, filename: str):
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the dcoument")
    for char, count in character_count.items():
        print(f"The '{char}' character was found {count}")

if __name__ == "__main__":
    main()