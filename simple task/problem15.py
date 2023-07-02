# Write A Program To Get 6 Number In The List And Display All Number And Then Clear List And Then Display
# Write A Program To Get 6 Number In The TUPLE And Display All Number And Then Clear TUPLE And Then Display

def problem15():
    n = int(input("enter number of elements: "))
    list1 = []
    for i in range(1, n + 1):
        e = int(input(f"enter element {i}: "))
        list1.append(e)
    print(list1)

    list1.clear()
    print("list after clearing: ", list1)

    print("tuple")

    tuple1 = ()
    for i in range(1, n + 1):
        e = int(input(f"enter element {i}: "))
        tuple1 += (e,)
    print(f"tuple: {tuple1}")
    list1 = list(tuple1)
    print(f"list: {list1}")
    list1.clear()
    print(f"list after clearning: {list1}")

    tuple1 = tuple(list1)
    print(f"tuple after convertion n clearning: {tuple1}")

problem15()