import string

def is_pangram(s):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if not letter in s.lower():
            return False

    return True
