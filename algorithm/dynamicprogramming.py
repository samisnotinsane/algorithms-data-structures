class Fibonacci:
    def __init__(self) -> None:
        self.cache = {}


    def naive(self, n: int) -> int:
        if n <= 1:
            return n

        return self.naive(n-1) + self.naive(n-2)
    
    def fast(self, n: int) -> int:
        if n <= 1:
            return n

        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.fast(n-1) + self.fast(n-2)
        
        return self.cache[n]
