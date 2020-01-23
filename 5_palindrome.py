def is_palindrome(word):
    chars = list(word)
    chars.reverse()
    reversed_word = "".join(chars)
    return word.lower() == reversed_word.lower()
    



# Tester
print(is_palindrome("mom"), True)
print(is_palindrome("Häst"), False)
print(is_palindrome("Anna"), True)
