import re

def is_palindrome(string):

    """
    Returns True if the given string is a palindrome, False otherwise.

    A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

    :param string str: The string to check for being a palindrome
    :return: True if the given string is a palindrome, False otherwise
    """
    
    # Remove all non-alphanumeric characters from the string
    cleaned_string = re.sub(r'\W+', '', string)

    # Convert the cleaned string to lowercase
    cleaned_string = cleaned_string.lower()

    # Reverse the cleaned string
    reversed_string = cleaned_string[::-1]

    # Check if the cleaned string is equal to its reversed version
    return cleaned_string == reversed_string

# @ example
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("12321"))  # True
print(is_palindrome("12345"))  # False
