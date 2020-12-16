import database
import datetime
from tkinter import *

def AskIDs(root):
    """This function gets the user to enter the member ID and the book ID and then once the button is clicked, the
    function checkIDs is run

    Parameters: root - allows the AskIDs function to interact with the tkinter window
    """
    data = database.GetDataFromFile()
    memberID = StringVar()
    bookID = StringVar()
    label1 = Label(root, text="Enter borrower's member-ID:", font=("Arial", 15))
    label1.pack()
    entry1 = Entry(root, textvariable=memberID)
    entry1.pack()
    label2 = Label(root, text="Enter the ID of the book they wish to withdraw:", font=("Arial", 15))
    label2.pack()
    entry2 = Entry(root, textvariable=bookID)
    entry2.pack()
    # Runs the command checkIDs once the button is clicked, and passes it the variables: root, data, memberID and bookID
    button = Button(root, text="Withdraw Book", command= lambda : checkIDs(root, data, str(memberID.get()), str(bookID.get())))
    button.pack()

def checkIDs(root, data, memberID, bookID):
    """This function receives the member ID and the book ID entered along with all the data in database.txt. It checks
    that the book ID and the member ID are valid and then runs the withdrawBook function

    Parameters: root - allows the checkIDs function to interact with the tkinter window
                data - contains all of the data within database.txt
                memberID - contains the member ID entered by the user
                bookID - contains book ID entered by the user
    """
    CorrectBookID = False
    CorrectMemberID = False
    for item in data:
        if item[0] == bookID:
            CorrectBookID = True
    try:
        if int(memberID) >= 1000 and int(memberID) <= 9999:
            CorrectMemberID = True
        else:
            text1 = Label(root, "Invalid member ID", font=("Arial", 15))
            text1.pack()
    except:
        ValueError
    # Verifies that valid book IDs and member IDs are entered
    if not CorrectBookID:
        text2 = Label(root, text="Invalid book ID", font=("Arial", 15))
        text2.pack()
    if CorrectBookID and CorrectMemberID:
        withdrawBook(memberID, bookID, data, root)

def withdrawBook(memberID, bookID, data, root):
    """This receives the member ID, the book ID, and the data from the text file. It then loops through all the data
    until it finds the correct book ID. Then it checks whether the member ID assigned to the book is 0 (meaning it is
    not checked out) and if it is, then it is replaced by the member ID and the book checked out. Otherwise, the book
    isn't checked out and a message is output to the user

    Parameters: root - allows the withdrawBook function to interact with the tkinter window
                data - contains all of the data within database.txt
                memberID - contains the member ID entered by the user
                bookID - contains book ID entered by the user
    """
    for item in data:
        if item[0] == bookID:
            if item[4] == '0':
                item[4] = memberID
                text1 = Label(root, text="Book withdrawn", font=("Arial", 15))
                text1.pack()
                database.WriteToFile(data)
                logfileData = database.GetDataFromLogfile()
                checkoutDate = (datetime.datetime.now()).strftime("%d/%m/%y")
                # Gets the date from the computer and converts it into day/month/year format
                newEntry = [bookID, checkoutDate, "0/0/00"]
                logfileData.append(newEntry)
                # Creates a new entry and adds it to logfile.txt
                database.WriteToLogfile(logfileData)
                
            else:
                text2 = Label(root, text="Book not available due to already being on loan", font=("Arial", 15))
                text2.pack()
