def get_factors(num):
    """Factors generator"""
    old_divisor = 0
    for factor in range(1, num):
        if num % factor == 0:
            divisor = int(num / factor)
            if old_divisor == factor:
                break
            old_divisor = divisor
            yield factor
            if divisor != factor:
                yield divisor


def main(num=13195):
    """The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    prime_factors = list()
    for factor in get_factors(num):
        if factor == 1:
            continue
        isPrime= True
        for _fac in get_factors(factor):
            if _fac not in [1, factor]:
                isPrime = False
                break
        if isPrime:
            prime_factors.append(factor)
    print(prime_factors)


if __name__ == '__main__':
    main(600851475143)
    # main()

