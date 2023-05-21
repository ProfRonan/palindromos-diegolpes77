"""Main functions"""


def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    return False

def is_palindrome(string):
   
    cleaned_string = ''.join(c.lower() for c in string if c.isalnum())

   
    return cleaned_string == cleaned_string[::-1]
