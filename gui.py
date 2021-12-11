from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import manage_database as database
import shutil


def openApplicantGUI():
    global emailVariable, nameVariable, cityVariable, addressVariable, educationVariable, employmentVariable, filename
    #TkInter
    root = Tk()

    title = Label(root, text="B.R.E.A.K.").grid(column=0, row=0, padx=100)
    description = Label(root, text="Enter Resume and Information to Send to Recruiters").grid(column=0, row=1, padx=100)

    emailVariable = StringVar()
    emailLabel = Label(root, text="Email: ").grid(column=0, row=2)
    email = Entry(root, textvariable=emailVariable).grid(column=0, row=3)

    nameVariable = StringVar()
    nameLabel = Label(root, text="Name: ").grid(column=0, row=4)
    name = Entry(root, textvariable=nameVariable).grid(column=0, row=5)

    cityVariable = StringVar()
    cityLabel = Label(root, text="City: ").grid(column=0, row=6)
    city = Entry(root, textvariable=cityVariable).grid(column=0, row=7)

    addressVariable = StringVar()
    addressLabel = Label(root, text="Address: ").grid(column=0, row=8)
    address = Entry(root, textvariable=addressVariable).grid(column=0, row=9)

    educationVariable = StringVar()
    educationLabel = Label(root, text="Education: ").grid(column=0, row=10)
    education = Entry(root, textvariable=educationVariable).grid(column=0, row=11)

    employmentVariable = StringVar()
    employmentLabel = Label(root, text="Employment: ").grid(column=0, row=12)
    employment = Entry(root, textvariable=employmentVariable).grid(column=0, row=13)


    #file chooser
    filename  = None
    def chooseFile():
        global filename

        fileTypes = (
                ('pdf files', '*.pdf'),
                ('All files', '*.*')
            )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=fileTypes)

        showinfo(
            title='Selected File',
            message=filename
        )

    resumeButton = Button(text="Open Resume", command=chooseFile).grid(column=0, row=14, pady=50)
    submitButton = Button(text="Submit", command=submit).grid(column=0, row=15,pady=10)


def submit():
    #global emailVariable, nameVariable, cityVariable, addressVariable, educationVariable, employmentVariable
    
    emailText = emailVariable.get()
    nameText = nameVariable.get()
    cityText = cityVariable.get()
    addressText = addressVariable.get()
    educationText = educationVariable.get()
    employmentText = employmentVariable.get()

    if (emailText is None or nameText is None or cityText is None or addressText is None or filename is None or educationText is None or employmentText is None):
        print("Something is not filled")
        return
    
    pdfPath = "./pdfs/" + emailText + ".pdf"
    shutil.copyfile(filename, pdfPath)
    database.add_entry(database.create_uuid(), nameText, emailText, educationText, employmentText, pdfPath)
    




