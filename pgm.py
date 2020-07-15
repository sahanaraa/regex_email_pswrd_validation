import re


mail = re.compile(r"(^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}$)")

password = re.compile(r"[a-zA-Z0-9_#$%]{8,}\d")

while True:
    user_email = str(input('enter a valid email:'))
    user_password = str(input("enter an email with atleast 8 characters long and end with a digit:"))

    check_email = mail.fullmatch(user_email)

    check_pswrd = password.fullmatch(user_password)

    if str(check_pswrd) and str(check_email) == "None":
        print("enter a valid mail id and password")
    else:
        print("you're all setup")
        break
    continue
