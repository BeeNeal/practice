def replace_vowels(string):

    vowels = set(['a', 'e', 'i', 'o', 'u'])

    for c in string:
        if c in vowels:
            string = string.replace(c, '*')
    return string

print replace_vowels('aladiee')