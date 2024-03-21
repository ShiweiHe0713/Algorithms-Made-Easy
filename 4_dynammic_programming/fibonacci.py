'''
Fibonacci: Using dynammic programming
'''

class Fibonacci:
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("Fibonacci sequence number can't be negative!")
        self.n = n
        self.memo = [None] * (n+1)

    def fibonacci_bf(self) -> int:
        '''Brute force recursion'''
        if self.n == 0: return 0
        if self.n == 1: return 1
        return Fibonacci(self.n-1).fibonacci_bf() + Fibonacci(self.n-2).fibonacci_bf()

    def fibonacci_table(self) -> int:
        '''Tabulation (Bottom-Up) Approach'''
        n = self.n
        table = [None] * (n+1)
        table[0] = 0
        table[1] = 1
        for i in range(2, n+1):
            table[i] = table[i-1] + table[i-2]
        return table[n]

    @staticmethod
    def fibonacci_dp(n: int, memo: list[int] = None) -> int:
        '''Memoization (Top-Down)'''
        if memo is None:
            memo = [None] * (n+1)
        if n == 0: return 0
        if n == 1: return 1
        if memo[n] is None:
            memo[n] = Fibonacci.fibonacci_dp(n-1, memo) + Fibonacci.fibonacci_dp(n-2, memo)
        return memo[n]

f1 = Fibonacci(10)
print(f1.fibonacci_bf())
print(f1.fibonacci_table())
print(f1.fibonacci_dp(10))
