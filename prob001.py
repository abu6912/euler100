def main(max_num=10):
    print(sum(num for num in range(max_num) if num % 3 == 0 or num % 5 == 0))


if __name__ == '__main__':
    main(1000)

