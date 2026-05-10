student_name=input("plese enter your name =")
academic_score=float(input("Enter your academic score ="))
attandance_score=float(input("Enter your attandance score ="))
extracurricular_Participation=input("Have you done extracurricular activity.\n give your answer in 'yes' or 'no' :")

if academic_score>=60 and attandance_score>=75 and extracurricular_Participation=="yes":
    print("you are eligable for interview")
else:
    print("you are not eligable for interview")