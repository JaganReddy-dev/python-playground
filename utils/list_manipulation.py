def list_manipulation(lst: list) -> list:
    """
    Docstring for list_manipulation function.

    :param lst: Accepts a list object
    :type lst: list
    :return: List containing length, reversed list, sorted list, unique elements, last two elements, and first four elements
    :rtype: list
    """
    length = len(lst)
    reversed_lst = lst[::-1]
    sorted_lst = sorted(lst)
    unique_elements = list(set(lst))
    last_two_el = lst[-2:] if length >= 2 else f"less than 2 elements: {lst}"
    first_four_el = lst[:4] if length >= 4 else f"less than 4 elements: {lst}"
    return [
        length,
        reversed_lst,
        sorted_lst,
        unique_elements,
        last_two_el,
        first_four_el,
    ]
