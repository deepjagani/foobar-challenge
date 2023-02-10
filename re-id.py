#foobar challenge 1 (Level 1) re-id

def solution_1_1(a):
    n = 23500
    primes = [True for i in range(n+1)]
    start = 2
    while (start * start <= n):
        if (primes[start] == True):
            for i in range(start * start, n+1, start):
                primes[i] = False
        start += 1
    prime_numbers = []
    for p in range(2, n+1):
        if primes[p]:
            prime_numbers.append(p)

    nums_string = "".join([str(x) for x in prime_numbers])
    return nums_string[a : a+5]
