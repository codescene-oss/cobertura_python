def count_chars(text):
    """
    Count the number of characters in a string.

    Args:
        text (str): The input string to count characters from

    Returns:
        int: The number of characters in the string
    """
    return len(text)

def count_vowels(text):
    """
    Count the number of vowels in a string.

    Args:
        text (str): The input string to count vowels from

    Returns:
        int: The number of vowels (a, e, i, o, u) in the string (case-insensitive)
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    # Example usage
    # bla
    sample_text = "Python is awesome!"
    result = count_chars(sample_text)
    print(f"The string '{sample_text}' has {result} characters.")
    result = count_vowels(sample_text)
    print(f"The string '{sample_text}' has {result} vowels.")
