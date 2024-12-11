#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Caesar Ghazi
"""

def sequential_list(length):
    """
    Prints a sequential list based on a given number
    
    Parameters:
    length : The length of the wanted list 

    Returns:
    list: the list after the entire operation is done

    Examples:
    >>> sequential_list(5)
    [0, 1, 2, 3, 4]
    >>> sequential_list(0)
    []
    >>> sequential_list(-3)
    []
    
    """
    
    list = []
    next_number = 0
    while len(list) < length:
        list.append(next_number)
        next_number = next_number + 1

    return list
