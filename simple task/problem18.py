# Write A Python Program to store name, address, contact in dictionary, and then update user contact number,  but user will enter his/her contact number at run time.

def problem18():
    info = {"name": "Srish", "address": "Punjab", "contact": 8437866002}
    print(info)
    # info.update({"contact":9876065314})
    # print("after update", info)
    contact = input("Enter new contact number: ")
    info["contact"] = contact
    print(info)
problem18()