def primes(n):
    """
    >>> primes(11)
    [1, 11]
    >>> primes(100)
    [1, 2, 2, 5, 5]
    >>> primes(1)
    [1]
    >>> primes(-1)
    Traceback (most recent call last):
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.primes[3]>", line 1, in <module>
        primes(-1)
      File "/Users/boqianfan/Desktop/q4.py", line 14, in primes
        raise ValueError("n must be > 0, because prime number has to be greater than 1")
    ValueError: n must be > 0, because prime number has to be greater than 1
    """

    #reference on stackoverflow : https://stackoverflow.com/questions/16996217/prime-factorization-list

    if n <= 0:
        raise ValueError("n must be > 0, because prime number has to be greater than 1")

    primeFactor = []
    primeFactor.append(1)
    i = 2
    while n >= i * i:
        while (n % i) == 0:
            primeFactor.append(i)
            n /= i
        i = i + 1
    if n > 1:
       primeFactor.append(n)
    return primeFactor

print primes(33)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
