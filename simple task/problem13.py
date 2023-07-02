# Write Python Program To Get Password From User And Make Sure That Password Should Contain Number And Alphabetic AND Password Length Should Not Be Greater Than Or Equal To 8

def problem13():
    password = input("enter pass: ")
    if password.isalnum() and len(password) >= 8:
        print("eligible")
    else:
        print("not eligible")
problem13()