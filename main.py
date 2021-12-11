#import libraries / modules
import pdfplumber
import os
import PyPDF2 
import io


#authorname = input("What is your Full Name (First, Last): ")
#authoremail = input("What is your email?: ")
#authorcity = input("What is your city?: ")
#authoraddress = input("What is your address?: ")

authorname = "Aditya Sen"
authoremail = "adityasen120@gmail.com"
authorcity = "Oakville, Ontario"
authoraddress = "1050 Falgarwood Dr., Apt #128, Oakville, Ontario L6H 2P3"

with pdfplumber.open("Aditya Sen Resume - High School-converted.pdf") as pdf:

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


# makes list_of_text into a new file
with io.open("NewFile(applicant " + number + ").txt", "w",encoding="utf-8") as f:
    print(list_of_text)
    # edits the file to have the name and email redacted
    f.write(list_of_text)
    


with io.open("OriginalFile(applicant " + number + ").txt", "w",encoding="utf-8") as f:
    # replace back the redacted information
    list_of_text = list_of_text.replace("[Applicant's Name]", authorname)
    list_of_text = list_of_text.replace("[Applicant's Email]", authoremail)
    list_of_text = list_of_text.replace("[Applicant's City]", authorcity)
    list_of_text = list_of_text.replace("[Applicant's Address]", authoraddress)
    
    f.write()





# make a new file with the redacted text based on the applicantfile