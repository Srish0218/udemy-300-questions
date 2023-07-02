# Write A Python Program to get 6 subject marks from the user and calculate total, average and percentage of that marks. And display to user.
def program10():
    sub1 = int(input("Marks of subject1: "))
    sub2 = int(input("Marks of subject2: "))
    sub3 = int(input("Marks of subject3: "))
    sub4 = int(input("Marks of subject4: "))
    sub5 = int(input("Marks of subject5: "))
    sub6 = int(input("Marks of subject6: "))
    total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
    print("total: ", total)
    average = total / 6
    print("average: ", average)

program10()