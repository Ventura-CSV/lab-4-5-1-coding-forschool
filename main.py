import random


def main():

    numbers = []
    total = 0
    i = 0
    while total < 5:
        num = random.random(0,100)
        numbers.append(num)
        i += 1


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
