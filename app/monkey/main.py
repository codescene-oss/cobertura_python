def count_chars(text):
    """
    Count the number of characters in a string.

    Args:
        text (str): The input string to count characters from

    Returns:
        int: The number of characters in the string
    """
    return len(text)


if __name__ == "__main__":
    # Example usage
    # test
    sample_text = "Python is awesome!"
    result = count_chars(sample_text)
    print(f"The string '{sample_text}' has {result} characters.")