#!/usr/bin/python3
"""This module contain a function that multiplies two matrix"""


def matrix_mul(m_a, m_b):
    """matrix_mul function that multiplies two matrix
    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    # variables to verify if both m_a and m_b can be multiplied
    num_colum1 = 0
    num_row2 = 0
