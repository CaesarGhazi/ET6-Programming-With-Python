def less_or_sum(first_number, second_number):
    """
    Compares two numbers and returns the smaller number if the two are not equal or the sum of the numbers if they are equal.

    Parameters:
    first_number (int or float): The first number.
    second_number (int or float): The second number.

    Returns:
    int or float: The smaller of the two numbers, or their sum if they're equal.

    Examples:
    >>> less_or_sum(3, 5)
    3
    >>> less_or_sum(10, 4)
    4
    >>> less_or_sum(7, 7)
    14
    >>> less_or_sum(2.4, 2.6)
    14
    """
    if first_number < second_number:
        return first_number
    elif first_number > second_number:
        return second_number
    else:
        return first_number + second_number