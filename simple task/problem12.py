# Write a Python program to display following output using for loop

def problem12():
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    n = int(input("number number of rows: "))
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print("")

    # print("----------------")
    # for i in range(1,n+1):
    #     for j in range(n,0,-1):
    #         if j>i:
    #             print("",end="")
    #         else:
    #             print("*",end=" ")
    #     print("")
    # print('-----------------')



    for r in range(1, n + 1):
        for m in range(n, 0, -1):
            if m > r:
                print(" ", end=' ')
            else:
                print("*", end=' ')
        print(" ")

problem12()