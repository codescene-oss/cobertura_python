# test_cases/test_main.py

import sys
import os

# Add parent directory to path to import main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import count_chars


def test_count_chars():
    """Test cases for the count_chars function."""
    # Test case 1: Normal string
    assert count_chars("hello") == 5, "Failed: 'hello' should have 5 characters"
    print("✓ Test 1 passed: Normal string")

    # Test case 2: Empty string
    assert count_chars("") == 0, "Failed: Empty string should have 0 characters"
    print("✓ Test 2 passed: Empty string")

    # Test case 3: String with spaces
    assert count_chars("hello world") == 11, "Failed: 'hello world' should have 11 characters"
    print("✓ Test 3 passed: String with spaces")

    # Test case 4: String with special characters
    assert count_chars("test!@#") == 7, "Failed: 'test!@#' should have 7 characters"
    print("✓ Test 4 passed: String with special characters")

    # Test case 5: String with numbers
    assert count_chars("abc123") == 6, "Failed: 'abc123' should have 6 characters"
    print("✓ Test 5 passed: String with numbers")

    # Test case 6: Single character
    assert count_chars("a") == 1, "Failed: 'a' should have 1 character"
    print("✓ Test 6 passed: Single character")

    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    test_count_chars()