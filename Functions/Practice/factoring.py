def get_factors(n):
    factors = []
    for i in range (1, n+1):
        if n % i == 0:
            factors.append(i)
    return(factors)
print(get_factors(12))

def get_multiples(n, limit):
    multiples = []
    for i in range (1, limit + 3):
        if i % n == 0:
            multiples.append(i)
    return(multiples)
print(get_multiples(3,20))