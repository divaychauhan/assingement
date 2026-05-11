days=int(input("HOW MANY DAYS YOU BORROW THE BOOK"))
charge=0
if days<=5:
    charge=days*2
    print(charge)
elif 6<=days<=10:
    charge=days*3
    print(charge)
elif 11<=days<=15:
    charge=days*4
    print(charge)
elif days>15:
    charge=days*5
    print(charge)