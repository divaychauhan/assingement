print("we are going to check you are eligable or not eligible for loan")
print("For eligibilty we are going to cheak some points which are as follows" "\n1.age criteria" ,
      "\n2.monthly income" 
      "\n3.credit score"
      "\n4.outstanding debts")
age=int(input("Please enter your age ="))
monthely_income=int(input("Please enter your monthly income ="))
credit_score=int(input("PLESE enter your credit score ="))
outstanding_debt=int(input("Please enter your outstanding debt ="))
if age>=18 and age<=60 and monthely_income>=25000 and age>=18 and age<=60 and outstanding_debt<=10000:
      print("You are eligable for loan")
else:
      print("loan is rejected")
