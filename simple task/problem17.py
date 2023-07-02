# Write a Python program to show a message in this format using print function.
# Each character should one tab distance
# A
# B C
# D E F
# G H I J
# K L M N
# O P Q R S
# T U V W X Y

def problem17():
    global c
    a = 65
    rows = int(input("number of rows: "))
    for i in range(0, rows):
        for j in range(0, i + 1):
            c = chr(a)
            print(c, end=' ')
            a += 1
        print("\r")


problem17()