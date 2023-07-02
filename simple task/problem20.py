# Write A Python Program To Get 5 Number From User In Array And Sum All Number And Display and  find maximum number.
import array as arr


def problem20():
    global i
    global sum
    sum = 0
    a = arr.array('i', [])
    n = int(input("number of elements: "))
    for i in range(0, n):
        a.append(int(input(f"enter {i} elements: ")))

    print("Array: ", end="")
    for i in a:
        print(i, end=" ")
        sum += i

    print(f"\nSum: {sum}")

    max = a[0]

    for i in range(1, n):
        if a[i] > max:
            max = a[i]
        else:
            pass
    print(f"Max number: {max}")

    min = a[0]
    for i in range(1, n):
        if a[i] < min:
            min = a[i]
        else:
            pass

    print(f"Min number: {min}")

problem20()
