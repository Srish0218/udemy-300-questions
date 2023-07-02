# Write A Python Program To Get 2 Number From The User, And Display 2 Table For That Number.
def problem9():
    n = int(input("Enter the number: "))
    print(f"Table of {n}")
    for i in range(0, 11):
        m = i * n
        print(f"{n}*{i}={m}")

problem9()