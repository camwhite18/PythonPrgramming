import database
from tkinter import *

def searchForBook(root):
    """Gets the user to enter a book name in the entry box which when the button is clicked, is retrieved and stored in
    the variable BookName

    Parameters: root - allows the searchForBook function to interact with the tkinter window
    """
    BookName = StringVar()
    entry1 = Entry(root, textvariable=BookName)
    entry1.pack()
    # Stores the value entered into the entry box in the variable BookName, the 'lambda' command delays it being stored
    # until the button below the entry box is clicked
    button = Button(root, text="Search", command= lambda : outputData(root, str(BookName.get())))
    button.pack()

def outputData(root, BookName):
    """Uses a function from database.py to retrieve all the data and outputs the details of all the books with the same
    name as BookName into the tkinter window

    Parameters: root - allows the outputData function to interact with the tkinter window
                BookName - passes the name of the book entered by the user into the function
    """
    data = database.GetDataFromFile()
    text = Label(root, text="       ID |                                        Title |            "
                            "              Author | Purchase Date |  Member ID", font=("Arial", 15))
    text.pack(anchor=W)
    text2 = Label(root, text="-" * 123, font=("Arial", 15))
    text2.pack(anchor=W)
    for item in data:
        if item[1] == BookName:
            text3 = ("%10s |%40s |%30s |%19s |%15s" % (item[0], item[1], item[2], item[3], item[4]))
            text3 = Label(root, text=text3, font=("Arial", 15))
            text3.pack(anchor=W)

if __name__ == '__main__':
    searchForBook(root)