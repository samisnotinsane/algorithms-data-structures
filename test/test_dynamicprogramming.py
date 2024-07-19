from algorithm.dynamicprogramming import Fibonacci

class TestFibonacci:
    def test_naive_base_zero(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.naive(0) == 0
        
    def test_naive_base_one(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.naive(1) == 1
        
    def test_naive_xs(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.naive(2) == 1
        
    def test_naive_s(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.naive(5) == 5
        
    def test_naive_m(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.naive(25) == 75025
        
    def test_naive_l(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.naive(30) == 832040
        
    def test_naive_xl(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.naive(34) == 5702887
        
    def test_fast_base_zero(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.fast(0) == 0
        
    def test_fast_base_one(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.fast(1) == 1
        
    def test_fast_xs(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.fast(2) == 1
        
    def test_fast_s(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.fast(5) == 5
        
    def test_fast_m(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.fast(25) == 75025
        
    def test_fast_l(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.fast(30) == 832040
        
    def test_fast_xl(self) -> None:
        fibonacci = Fibonacci()
        assert fibonacci.fast(34) == 5702887
