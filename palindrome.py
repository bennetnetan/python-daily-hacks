import re

def is_palindrome(string):
    """Check if a given string is a palindrome.

    A palindrome is a word, phrase, number or other sequence of characters that reads
    the same forward and backward (ignoring spaces, punctuation, and capitalization).

    Parameters
    ----------
    string : str
        The string to check.

    Returns
    -------
    bool
        Whether the string is a palindrome or not.

    Examples
    --------
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("12321")
    True
    >>> is_palindrome("12345")
    False
    """
    
    # Remove all non-alphanumeric characters from the string and convert it to lowercase

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
