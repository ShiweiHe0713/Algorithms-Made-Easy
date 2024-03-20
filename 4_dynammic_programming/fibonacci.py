'''
Fibonacci: Using dynammic programming
'''

class fibonacci:
    def __init__(self, n: int):
        self.memo = []
        self.n = n

    def fibonacci_bf(self) -> int:
        '''Brute force recursion'''
        n = self.n
        if self.n == 0: return 1
        if self.n == 1: return 1
        return fibonacci(n-1).fibonacci_bf() + fibonacci(n-2).fibonacci_bf()

    def fibonacci_table(self) -> int:
        pass

    def fibonacci_dp(self,n : int) -> int:
        n = self.n
        self.memo = [0] * (n+1)
        if n == 0:
            self.memo[0] = 1
            return 1
        if n == 1: 
            self.memo[1] = 1
            return 1
        
        self.memo[n] = self.memo[n-1] + self.memo[n-2]
        return self.fibonacci_dp(n-1) + self.fibonacci_dp(n-2)

f1 = fibonacci(10)
print(f1.fibonacci_bf())
