#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Caesar Ghazi
"""
def iterations_list(number_of_iterations, start_number):
    """
    Prints a sequential list based on a given number of iterations and a starting number
    
    Parameters:
    number_of_iterations : number of times of iteration
    start_number : The starting number of the list 

    Returns:
    new_list: the list after the entire operation is done

    Examples:
    >>> iterations_list(3,2)
    [2,3,4]
    >>> iterations_list(0, 5)
    []
    >>> iterations_list(3, -3)
    [-3, -2, -1]
    
    """
    if number_of_iterations == 0:
        return []

    new_list = []
    while len(new_list) < number_of_iterations:
        new_list.append(start_number)
        start_number = start_number + 1

    return new_list
