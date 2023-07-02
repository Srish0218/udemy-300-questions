
# Write A Program To Show Such Type Of Layout Of Number And Square.


def problem1():
    # problem 1
    n = int(input("NO. of numbers: "))

    # declare dictionary
    numbers = {}

    # run loop from 1 to n
    for i in range(1, n + 1):
        numbers[i] = i * i

    # print dictionary
    print(numbers)

    print("Number \t\t Square")
    print(i," \t\t ",numbers[i])

problem1()
