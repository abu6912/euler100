def fib(max_fib_value):
    """Fibonacci generator"""
    a, b = 0, 1
    while a <= max_fib_value:
        yield a
        a, b = b, a + b


def main(max_fib_value=10):
    """ Each new term in the Fibonacci sequence is generated by adding the
     previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    """
    print(sum(fib_num for fib_num in fib(max_fib_value) if fib_num % 2 == 0))


if __name__ == '__main__':
    main(4 * (10**6))

