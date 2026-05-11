print("ENTER the brand name of car you want to purchase")
brand=input("Enter the brand name =")
price=float(input("enter the price ="))
tax = 0

if brand == "Mahindra":
    if price >= 7 and price <= 10:
        tax = price * 0.05

elif brand == "Audi":
    if price >= 10 and price <= 15:
        tax = price * 0.10

elif brand == "Jaguar":
    if price >= 15 and price <= 20:
        tax = price * 0.25

elif brand == "Mercedes":
    if price >= 20 and price <= 25:
        tax = price * 0.30

else:
    print("Invalid car brand")

print("Tax on car purchase =", tax)