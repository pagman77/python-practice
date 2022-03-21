def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_list = phrase.lower()
    phrase_list = list(phrase_list)
    phrase_list_char = [ltr for ltr in phrase_list if ltr != " "]
    phrase_list = phrase_list_char.copy()
    phrase_list_char.reverse()
    return phrase_list == phrase_list_char
