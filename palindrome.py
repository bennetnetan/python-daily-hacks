import re

def is_palindrome(string):
    cleaned_string = re.sub(r'[A-za-z0-9]', '', string).lower()
    return cleaned_string == cleaned_string[::-1]

