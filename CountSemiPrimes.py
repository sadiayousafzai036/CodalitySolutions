def primeSieve(N):
    # first assume that numbers from 0 to N are all prime numbers
    prime_sieve = [True] * (N + 1)
    # special case
    prime_sieve[0] = prime_sieve[1] = False
    # algorithm to find numbers that are not prime numbers
    i = 2
    while (i * i <= N):
        if prime_sieve[i]:
            k = i * i
            while (k <= N):
                prime_sieve[k] = False
                k += i
        i += 1

    return prime_sieve


def partialSemiprime(N):
    prime_sieve = primeSieve(N)
    # primes vector to store all the prime numbers
    primes = []
    for i in range(len(prime_sieve)):
        if prime_sieve[i]:
            primes.append(i)

    # first assume that numbers from 0 to N are NOT semiprime numbers
    semiprime_sieve = [False] * (N + 1)
    for i in range(len(primes)):
        if (i * i > N):
            break
        for j in range(i, len(primes)):
            if primes[i] * primes[j] > N:
                break
            semiprime_sieve[primes[i] * primes[j]] = True

    partial_semiprime = []
    count = 0
    for x in semiprime_sieve:
        if x:
            count += 1
        partial_semiprime.append(count)

    return partial_semiprime


def solution(N, P, Q):
    # write your code in Python 2.7
    partial_semiprime = partialSemiprime(N)
    result = []
    M = len(P)
    for i in range(M):
        result.append(partial_semiprime[Q[i]] - partial_semiprime[P[i] - 1])

    return result

print(solution(26, [1, 4, 16], [26, 10, 20]))

# 4, 6, 9, 10, 14, 15, 21, 22, 25, 26
#[0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 7, 8, 8, 8, 9, 10]
