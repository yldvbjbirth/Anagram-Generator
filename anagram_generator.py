def generate_anagrams(word):
    """
    Generate all possible anagrams of the given word.

    Args:
        word (str): The input word.

    Returns:
        set: A set containing all unique anagrams of the word.
    """
    if len(word) <= 1:
        return {word}
    anagrams = set()
    for i, letter in enumerate(word):
        remaining = word[:i] + word[i+1:]
        for sub_anagram in generate_anagrams(remaining):
            anagrams.add(letter + sub_anagram)
    return anagrams

if __name__ == "__main__":
    input_word = input("Enter a word: ")
    results = generate_anagrams(input_word)
    print(f"Anagrams of '{input_word}':")
    for a in sorted(results):
        print(a)
