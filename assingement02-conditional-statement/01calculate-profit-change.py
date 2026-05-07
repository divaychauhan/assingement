cost_price=int(input("Enter the cost price ="))
selling_price=int(input("Enter the selling price="))
if selling_price>cost_price:
    profit=selling_price-cost_price
    print("your profit is =",profit)
else:
    loss=cost_price-selling_price
    print("your loss is =",loss)
print("if you want to show your percentage in profit or loss,enter percentage ")
message=input("Enter here =")
if message == "percentage":
    print("NOW YOU ARE SHOWING YOUR PROFIT PERCENTAGE")
else:
    print("invalid credential")
if selling_price>cost_price:
    profit_percentage=profit*100//cost_price
    print("your profit percentage is =",profit_percentage)
else:
    loss_percentage=loss*100//cost_price
    print("your loss percentage is =",loss_percentage)
    