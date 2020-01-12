def get_prime_factors(num, factor=1, out_list=[]):
    """Prime Factors generator"""
    while factor <= num:
        factor += 1
        if num % factor == 0:
            divisor = int(num/factor)
            out_list.append(factor)
            get_prime_factors(divisor, factor=1, out_list=out_list)
            break
    return out_list


def main(max_num=10):
    """2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the
     numbers from 1 to 20?
    """
    prime_factor_dict = dict()
    for num in range(2, max_num+1):
        prime_factor_list = get_prime_factors(num, factor = 1, out_list = [])
        temp_dict = {
            factor: prime_factor_list.count(factor)
            for factor in set(prime_factor_list)
        }
        for factor in set(prime_factor_list):
            if factor not in prime_factor_dict.keys():
                prime_factor_dict[factor] = prime_factor_list.count(factor)
            elif prime_factor_dict[factor] < prime_factor_list.count(factor):
                prime_factor_dict[factor] = prime_factor_list.count(factor)

    # print(prime_factor_dict)
    product = 1
    for factor, power in prime_factor_dict.items():
        product *= factor ** power
    print(product)


if __name__ == '__main__':
    main(20)

