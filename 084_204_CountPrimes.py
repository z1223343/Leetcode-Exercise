"""
1 level solution:

1. math: sieve of eratosthenes
"""
# solution 1:
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        primes = [True]*n
        primes[0] = primes[1] = False
        for i in range(2,int(n**0.5)+1):
            if primes[i] == True:
                primes[i**2:n:i] = [False]*len(primes[i**2:n:i])  # 可以这样啊
        return sum(primes)  # 也可以这样啊



"""
知识点：1不是质数。
"""