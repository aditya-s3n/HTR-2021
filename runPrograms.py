import gui
import whattofilterfor

Continue = True

while Continue:
    choice = input("Are you an applicant (0) or a recruiter (1)?, ")
    if choice == "0":
        gui.openApplicantGUI()
    elif choice == "1":
        whattofilterfor.searchForApplicant()
    else:
        print("Not a valid input")
    
    continueQuestion = input("Continue (Y/N), ")

    if continueQuestion.lower() == "n":
        Continue = False
    else:
        Continue = True

print("Exiting Program...")