print("we are goging to check how many years left in your retirement")
retirement_age=65
age=int(input("Enter your age ="))
reaming_year=retirement_age-age
if age==retirement_age:
    print("you have already reached retirement age.")
else:
    print("Remaning years in retirement is = ",reaming_year)