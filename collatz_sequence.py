def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result


def main():
    while True:
        try:
            user_input = input('Enter number: ')
            number = int(user_input)
            break
        except ValueError:
            print("You must enter an integer.")

    while number != 1:
        number = collatz(number)


if __name__ == "__main__":
    main()
