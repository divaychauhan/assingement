
age = int(input("Enter your age: "))
graduate = input("Are you a graduate? (yes/no): ")
nationality = input("Enter your nationality: ")

if age >= 21 and age <= 32:
    
    if graduate == "yes":
        
        if nationality == "Indian":
            print("You are eligible for UPSC.")
            print("Proceed to Prelims Exam")

            prelims_score = int(input("Enter Prelims score: "))
            prelims_cutoff = 100

        
            if prelims_score >= prelims_cutoff:
                print("You passed the Prelims.")
                print("Proceed to Mains Exam")

                mains_score = int(input("Enter Mains score: "))
                mains_cutoff = 200

                
                if mains_score >= mains_cutoff:
                    print("You passed the Mains.")
                    print("Proceed to Interview")

                    interview_score = int(input("Enter Interview score: "))
                    interview_cutoff = 50

                    
                    if interview_score >= interview_cutoff:
                        print("Congratulations! You have cleared the UPSC.")
                    else:
                        print("You failed the Interview.")

                else:
                    print("You failed the Mains.")

            else:
                print("You failed the Prelims.")

        else:
            print("You are not eligible because nationality must be Indian.")

    else:
        print("You are not eligible because you are not a graduate.")

else:
    print("You are not eligible because age must be between 21 and 32.")
        
    