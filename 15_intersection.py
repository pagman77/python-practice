def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    s1 = set(l1)
    s2 = set(l2)
    intersection = s1 & s2
    return list(intersection)

    # could also be : [num for num in s1 if num in s2]
