#Write A Python Program To Get 3 Number From The User And Display Maximum Number

def problem11():
    a = int(input("1st number: "))
    b = int(input("2nd number: "))
    c = int(input("3rd number: "))

    #for 2 number---------------
    # print("maximum number is: ")
    #
    # if a>b:
    #     print(a)
    # else:
    #     print(b)
    #---------------------

    maxi = max(a, b, c)
    print("maximum number is: ")
    print(maxi)

problem11()
