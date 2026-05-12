

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


if num1 >= num2 and num1 >= num3:

    if num2 >= num3:
        print("Numbers in Descending Order:", num1, num2, num3)
    else:
        print("Numbers in Descending Order:", num1, num3, num2)

elif num2 >= num1 and num2 >= num3:

    if num1 >= num3:
        print("Numbers in Descending Order:", num2, num1, num3)
    else:
        print("Numbers in Descending Order:", num2, num3, num1)

else:

    if num1 >= num2:
        print("Numbers in Descending Order:", num3, num1, num2)
    else:
        print("Numbers in Descending Order:", num3, num2, num1)