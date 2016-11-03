def isPrime(n):
    for i in range(2,n-1):
        if(n%i==0):
            return False
        return True

def firstNPrimes(n):
    primes = []
    origin = 0
    while len(primes) < n:
        origin += 1
        if isPrime(origin) == True:
            primes.append(origin)
    return primes

print(firstNPrimes(5))
print(firstNPrimes(10))
print(firstNPrimes(15))
print(firstNPrimes(99))
