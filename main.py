#import libraries / modules
import pdfplumber
import os
import PyPDF2 
import io
import manage_database as database

# so this gets the file and the input from the user, then it gets what the boss wants in terms of filtering
# then it returns the applicants who fit the criteria

#database.add_entry(database.create_uuid(), "Sebi", "sebi@email.com", "IRHS", "Pro Inter", "Aditya.pdf")

#import csvGenerator
matching_applicants = []
filtered_universities = ["iroquois ridge high school", "fseesfesfsehfuiohskfljsjkljkl"]
filtered_employment = ["model"]




#authorname = input("What is your Full Name (First, Last): ")
authoremail = input("What is your email?: ")
#authorcity = input("What is your city?: ")
#authoraddress = input("What is your address?: ")

# from database, get the authorname, authoremail, authorcity, authoraddress, authorpostalcode

entry = database.get_entry_by_email(authoremail)
if entry is None:
    print("Applicant not found in the database")
else:
    print(entry)
    
#authorname = entry[
#authoremail = entry[
#authorcity = entry[


authorname = "Aditya Sen"
authoremail = "sebi@email.com"
authorcity = ""
authoraddress = "1050 Falgarwood"
authorpostalcode = "L6H 2P3"

def use_applicant_path(applicant_path):
    with pdfplumber.open(applicant_path) as pdf:

        # gets all the pages of the pdf and puts it into a list
        for page in pdf.pages:
            list_of_text = page.extract_text()
            images = page.images
        

        # replaces the text in the pdf of biased information to blur information
        list_of_text = list_of_text.replace(authorname, "[Applicant's Name]")
        list_of_text = list_of_text.replace(authoremail, "[Applicant's Email]")
        list_of_text = list_of_text.replace(authorcity, "[Applicant's City]")
        list_of_text = list_of_text.replace(authoraddress, "[Applicant's Address]")
        


    # reads number.txt and converts it to an integer
    with open("number.txt", "r") as f:
        number = str(int(f.read()) + 1)

    # writes the number to number.txt
    with open("number.txt", "w") as f:
        f.write(str(number))




    # makes list_of_text into a new file in the directory applicant number
    with io.open("NewFile(applicant " + number + ").txt", "w",encoding="utf-8") as f:
        # edits the file to have the name and email redacted
        f.write(list_of_text)
        
    with io.open("OriginalFile(applicant " + number + ").txt", "w",encoding="utf-8") as f:
        # replace back the redacted information
        list_of_text = list_of_text.replace("[Applicant's Name]", authorname)
        list_of_text = list_of_text.replace("[Applicant's Email]", authoremail)
        list_of_text = list_of_text.replace("[Applicant's City]", authorcity)
        list_of_text = list_of_text.replace("[Applicant's Address]", authoraddress)
        f.write(list_of_text)
# makes a folder for the applicant



# puts both files into the applicant folder

        

# delete all the files so that aditya doesn't have to manually delete them
def delete_all_files(number):
    for i in range(1, int(number+1)):
        os.remove("NewFile(applicant " + str(i) + ").txt")
        os.remove("OriginalFile(applicant " + str(i) + ").txt")

        # make number.txt back to 0
    with open("number.txt", "w") as f:
        f.write("0")



# this works but has to be somewhere else to work
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

                
print("The following applicants have been found: ", end="")
for i in matching_applicants:
    print(i, end=",")





print(matching_applicants)
        
# used to delete all the files
#delete_all_files(int(number))