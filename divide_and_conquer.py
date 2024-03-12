import numpy as np
from typing import List
from numpy.linalg import matrix_power
from merge_sort import merge

def merge_sort(arr, l, r):
    '''
    T(n) = 2T(n/2) + n => Θ(nlogn)
    '''
    mid = l + (r - l) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid+1, r)
    merge(arr, l, mid, r)

def exponentiation_slow(a, n):
    '''
    Use a^n = a * a^(n-1)
    T(n) = Θ(n)
    '''
    if n == 1: return a
    return a * exponentiation_slow(a, n-1)

def exponentiation(a, n):
    '''
    input: a, n, output: a^n
    Using divide and conquer algorithm
    T(n) = T(n/2) + O(1) => Θ(logn)
    '''
    if n == 1: return a
    factor = exponentiation(a, n // 2)

    if n % 2 == 1:
        result = factor * factor * a
    else:
        result = factor * factor
    return result

def fibonacci_slow(n):
    '''Very slow'''
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

def fibonacci(n):
    '''
    F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1
    Using matrix multiplication, divide and conquer
    T(n) = O(logn)
    '''
    matrix = np.array([[1,1],[1,0]])
    result = matrix_power(matrix, n-1)
    return result[0][0]

def bit_multiply(a : List[int], b: List[int]) -> int:
    len_c = len(a) + len(b)
    c = [None] * len_c
    pass

def karatsuba(a, b):
    pass

def matrix_multiply(matrix_1, matrix_2):
    