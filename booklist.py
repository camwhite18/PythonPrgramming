import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
from database import GetDataFromLogfile, GetDataFromFile

def GetPopularBooks(root):
    """This function gets the data from the logfile using the function from database.py and stores the book names and
    the number of times withdrawn into lists. Once they are sorted by the bubble sort function, it outputs the list of
    books in popularity order then calls the function to create the graph.

    Parameters: root - allows the GetPopularBooks function to interact with the tkinter window
    """
    data = GetDataFromLogfile()
    popularBooks = []
    for item in data:
        if [item[0], 0] not in popularBooks:
            popularBooks.append([item[0], 0])

    for x in popularBooks:
        count = 0
        for i in data:
            if x[0] == i[0]:
                count +=1
        x[1] = count
    popularBooks = GetBookNames(popularBooks)
    # Gets all of the book names and how many times the books have been withdrawn and stores it in a list
    bookNames = []
    popularBooksOccurrence = []
    for book in popularBooks:
        if book[0] not in bookNames:
            bookNames.append(book[0])
            popularBooksOccurrence.append(book[1])
        else:
            pos = bookNames.index(book[0])
            popularBooksOccurrence[pos] += 1
    bookNames, popularBooksOccurrence = BubbleSort(bookNames, popularBooksOccurrence)
    books = "List of books in popularity order: "
    books = books + ", ".join(bookNames)
    text2 = Label(root,text=books, font=("Arial", 15), anchor=W)
    text2.pack()
    CreateGraph(bookNames, popularBooksOccurrence, root)

def GetBookNames(popularBooks):
    """This function uses a function from database.py to get all of the book data and then changes all of the book IDs
    in the list popularBooks to their corresponding names.

    Parameters: popularBooks - contains the list of the book IDs from logfile.txt
    """
    bookData = GetDataFromFile()
    for item in popularBooks:
        for x in bookData:
            if item[0] == x[0]:
                item[0] = x[1]
    return popularBooks

def CreateGraph(bookNames, popularBooksOccurrence, root):
    """This function uses the two lists passed to it as parameters, then creates a bar graph showing the most popular
    books, which is embedded into the tkinter window.

    Parameters: root - allows the searchForBook function to interact with the tkinter window
                bookNames - contains the list of popular book names
                popularBooksOccurrence - contains the list of the number of times each book has been withdrawn
    """
    plt = Figure(figsize=(5,5), dpi=100)
    a = plt.add_subplot(111)
    a.bar(bookNames,popularBooksOccurrence)
    a.set_xlabel("Books")
    a.set_ylabel("Loans")
    # Adds labels to the x and y axis of the graph
    yIncrement = range(min(popularBooksOccurrence), math.ceil(max(popularBooksOccurrence))+1)
    a.set_yticks(yIncrement)
    # Adds an increment to the y axis
    bar1 = FigureCanvasTkAgg(plt, root)
    bar1.draw()
    bar1.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
    # Creates the graph and embeds the graph in the tkinter window

def BubbleSort(bookNames, popularBooksOccurrence):
    """This function performs a bubble sort on the popularBooksOccurrence list and at the same time swaps the
    corresponding bookNames list around

    Parameters: bookNames - contains the unsorted list of book names
                popularBooksOccurrence - contains the unsorted list of the number of times each book has been withdrawn
    """
    length = len(popularBooksOccurrence)
    for x in range(length):
        for y in range(0, length-x-1):
            if popularBooksOccurrence[y] < popularBooksOccurrence[y+1]:
                popularBooksOccurrence[y], popularBooksOccurrence[y+1] = popularBooksOccurrence[y+1], popularBooksOccurrence[y]
                bookNames[y], bookNames[y+1] = bookNames[y+1], bookNames[y]
    # Performs a bubble sort on both lists
    return bookNames, popularBooksOccurrence

if __name__ =="__main__":
    # testing BubbleSort
    print(BubbleSort(["Book_1", "Book_2", "Book_3"], [1, 3, 2]))
    #testing CreateGraph
    CreateGraph(["Book_1","Book_2"],[3,1],root)