#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Caesar Ghazi
"""

def string_length(input_string):
    """
    Returns the length of the input if it is not empty. otherwise, returns None.

    Parameters:
    input_string : The input 

    Returns:
    int or None: The length of the input if it is not empty, or None if the input is empty.

    Examples:
    >>> string_length([])
    None
    >>> string_length([1, 2, 3])
    3
    >>> string_length("")
    None
    >>> string_length("hello")
    5
    """
    if len(input_string) == 0:
        return None

    return len(input_string)
