def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    # names = []
    # for person in people:
    #     first_name = person["first"]
    #     last_name = person["last"]
    #     names.append(f"{first_name} {last_name}")
    # return names

    # names.append(f"{first_name} {person["last"]}")
    # ^ didn't work because of double quotes in double quotes!!

    return [f"{person['first']} {person['last']}" for person in people]
