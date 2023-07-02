# Write a Python Program to calculate union of two set

def problem5():
    a=int(input("number of elements in set A: " ))
    b=int(input("number of elements in set B: " ))
    c = int(input("number of elements in set C: "))

    A=set()
    B=set()
    C = set()

    for i in range(1,a+1):
        e=input(f"element{i} of set A: ")
        A.add(e)

    for j in range(1,b+1):
        f=input(f"element{j} of set B: ")
        B.add(f)
    for k in range(1,c+1):
        f=input(f"element{k} of set C: ")
        C.add(f)

    print("SetA: ",A)
    print("SetB: ", B)
    print("SetB: ", C)
    print("Unions-----")
    U=A.union(B)
    Union= U.union(C)
    print("Union1: ",Union)
    Union2= A | B | C
    print("Union2: ",Union2)
    Union3= A.union(B,C)
    print("union3: ", Union3)
    print("intersection------")
    intersection=A.intersection(B,C)
    if intersection== set():
        print("intersection: null")
    else:
        print("intersection: ", intersection)

    print("difference----")
    diff1=A-B
    print("difference: ",diff1)

    symdiff1 = A.symmetric_difference(B)
    # Alternatively, you can use the ^ operator:
    # sym_diff = set1 ^ set2
    symdiff2=A^B
    print(symdiff1)
    print(symdiff2)

problem5()