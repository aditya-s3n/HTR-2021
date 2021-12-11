import manage_database as database
import AutoEmailer


def searchForApplicant():
    def filtered(entries):
        for i in range(len(entries)):
            entry = entries[i]
            print(f"{str(i)} : Education: {entry[3]}, Previous Experience / Previous Employment:{entry[4]}")

        number = input("Choose a number to schedule an interview, ")
        if not number.isdigit():
            print("Invalid input")
            return
        number = int(number)
        if not 0 <= number < len(entries):
            print("Invalid input")
            return
        entry = entries[number]
        email = entry[2]
        AutoEmailer.emailApplicant(email, entry[1])
        print("Emailed applicant succesfully!")




    #asks what to filter for based on keywords
    all = input("What do you want to filter for? Education, or employment? ").lower()

    if all == "education":
        education = input("What education do you want filter for? ")
        entries = database.get_entries_by_education(education)
        if len(entries) == 0:
            print("No entries found.")
        else:
            filtered(entries)
        

    elif all == "employment":
        employment = input("What employment do you want filter for? ")
        entries = database.get_entries_by_employment(employment)
        if len(entries) == 0:
            print("No entries found.")
        else:
            filtered(entries)






        # filters based on 


    """
    for i in range(1, int(number)+1):
        # look for speicific words in the text file
        with io.open("NewFile(applicant " + str(i) + ").txt", "r",encoding="utf-8") as f:

            text = f.read().lower()
            # filter for words of the university
            for university in filtered_universities:
                if university in text:
                    for employment in filtered_employment:
                        if employment in text:
                            matching_applicants.append("NewFile(applicant " + str(i) + ").txt")
                            break
    """