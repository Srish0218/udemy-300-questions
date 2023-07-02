# Write a program to get 6 number in the list and TUPEL and sum that number


def problem14():
    n = int(input("enter number of elements: "))
    list1 = []
    for i in range(1, n + 1):
        e = int(input(f"enter element {i}: "))
        list1.append(e)
    print(list1)
    print("sum: ", sum(list1))

    print("tuple")

    tuple1 = ()
    for i in range(1, n + 1):
        e = int(input(f"enter element {i}: "))
        tuple1 += (e,)
    print(tuple1)
    print("sum: ", sum(tuple1))

problem14()