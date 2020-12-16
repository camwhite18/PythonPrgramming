import database
import datetime
from tkinter import *

def returnBook(root):
    """This function gets the user to enter the book ID of the book they want to return. I does this through creating
     an entry box in the tkinter window then once the button below it is clicked, the value entered is retrieved and
     stored in the variable ReturnBookID

     Parameters: root - allows the returnBook function to interact with the tkinter window
     """
    ReturnBookID = StringVar()
    label2 = Label(root, text="Enter the ID of the book they wish to return:", font=("Arial", 15))
    label2.pack()
    entry1 = Entry(root, textvariable=ReturnBookID)
    entry1.pack()
    button = Button(root, text="Return", command=lambda: updateDatabase(root, str(ReturnBookID.get())))
    button.pack()

def updateDatabase(root, ReturnBookID):
    """This function gets the data from in database.txt and then loops through it until it finds the book with the same
    ID as that that is passed as a parameter to the function in ReturnBookID. If it does, then it checks that the
    member ID associated to it is not equal to 0 and it changes it to 0. If it is equal to 0, then an appropriate error
    message is shown

    Parameters: root - allows the updateDatabase function to interact with the tkinter window
                ReturnBookID - contains the book ID entered by the user
    """
    returned = False
    data = database.GetDataFromFile()
    for book in data:
        if book[0] == ReturnBookID and book[4] != "0":
            book[4] = "0"
            database.WriteToFile(data)
            returned = True
            logfileData = database.GetDataFromLogfile()
            for line in logfileData:
                if line[0] == ReturnBookID and line[2] == "0/0/00":
                    line[2] = (datetime.datetime.now()).strftime("%d/%m/%y")
            database.WriteToLogfile(logfileData)

    if returned:
        text1 = Label(root, text="Book returned", font=("Arial", 15))
        text1.pack()
    else:
        text2 = Label(root, text="Error: Book could not be returned", font=("Arial", 15))
        text2.pack()

if __name__ == '__main__':
    #Testing updateDatabase with an example book ID
    updateDatabase(root, "1")