import itertools


def main(num=2):
    """A palindromic number reads the same both ways. The largest palindrome
     made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    max_product = 0
    num3digits = range(10**(num-1), 10**num)
    for comb in itertools.permutations(num3digits, 2):
        product = comb[0] * comb[1]
        if str(product) == str(product)[::-1]:
            max_product = max(max_product, product)

    print(max_product)


if __name__ == '__main__':
    main(3)

