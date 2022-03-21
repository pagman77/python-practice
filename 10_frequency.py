def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """

    frequency_counter = {}
    for ltr in lst:
        if ltr not in frequency_counter:
            frequency_counter[ltr] = 1
        else:
            frequency_counter[ltr] += 1
    return frequency_counter.get(search_term, 0)
