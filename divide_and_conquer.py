import time

def exponentiation_1st_attempt(a, n):
    '''
    Use a^n = a * a^(n-1)
    T(n) = Θ(n)
    '''
    if n == 1: return a
    return a * exponentiation_1st_attempt(a, n-1)

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

start_time = time.time()
a = exponentiation_1st_attempt(2,1000)
print(a)
print(time.time() - start_time)
