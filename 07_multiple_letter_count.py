def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    frequency_counter = {}
    for ltr in phrase:
        if ltr not in frequency_counter:
            frequency_counter[ltr] = 1
        else:
            frequency_counter[ltr] += 1
    return frequency_counter

    #can solve with dictonary comprehension
