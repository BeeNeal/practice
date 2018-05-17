def string_validator(s):
    """Return t/f for if s contains lowers, uppers, digits, etc"""

    t = type(s)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print any(method(char) for char in s)