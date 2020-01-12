import itertools


def main(max_num=10):
    """The sum of the squares of the first ten natural numbers is,
        1^2+2^2+...+10^2 = 385
    The square of the sum of the first ten natural numbers is,
        (1+2+...+10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural
    numbers and the square of the sum is 3025−385 = 2640.
    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
    """
    print(sum(
        2 * comb[0] * comb[1]
        for comb in itertools.combinations(range(1, max_num+1), 2)
    ))


if __name__ == '__main__':
    main(100)

