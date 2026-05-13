

saved_phone = "1234567890"
saved_otp = "1234"

saved_email = "user@example.com"
saved_password = "password123"

print("1. Login with Phone")
print("2. Login with Email")
print("3. Exit")

choice = int(input("Enter your choice: "))


if choice == 1:
    phone = input("Enter phone number: ")
    otp = input("Enter OTP: ")

    if phone == saved_phone and otp == saved_otp:
        print("Login successful with phone!")
    else:
        print("Invalid phone number or OTP.")


elif choice == 2:
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == saved_email and password == saved_password:
        print("Login successful with email!")
    else:
        print("Invalid email or password.")


elif choice == 3:
    print("Exiting the program. Have a nice day!")


else:
    print("Invalid choice. Please select a valid option.")
