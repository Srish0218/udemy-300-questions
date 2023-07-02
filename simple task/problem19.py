# Write A Python Program To Get 3 Number From User And Put In The Following Equation:
# 	a+b+ca/b(2a + 3b)


def problem19():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = int(input("enter c: "))

    equ = (a + b + (c * a)) / b * (2 * a + 3 * b)
    print(equ)
problem19()