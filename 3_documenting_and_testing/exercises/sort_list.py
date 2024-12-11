#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Caesar Ghazi
"""
def sort_list(random_list, main_list=None):
    """
    Sorts a list the prints it
    
    Parameters:
    random_list: The list to be put in order
    main_list=None : The first part of the list which is set to none 

    Returns:
    main_list: the list in order

    Examples:
    >>> sort_list([1, 0, 4, 2, 3],)
    [0, 1, 2, 3, 4]
    >>> sort_list([],)
    []
    >>> sort_list([-6, -8, 5, 4, 7],)
    [-8, -6, 4, 5, 7]
    
    """
    if main_list is None:
        main_list = []
    while random_list:
        smallest_number = min(random_list)
        random_list.remove(smallest_number)
        main_list.append(smallest_number)
    return main_list
