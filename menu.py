from tkinter import *
import booksearch
import bookcheckout
import bookreturn
import booklist

def close_tk():
    """Closes the tkinter window and stops the program running
    """
    root.destroy()

def main():
    """Creates the main tkinter window that is used throughout the program and adds the title, and all of the buttons to
    the window which are used in operation of the system
    """
    root.wm_title("Library Manager")
    root.geometry("1500x700")
    text = Label(root, text="Welcome to the Library Manager", font=("Arial Bold", 40))
    text.pack()
    btn1 = Button(root, text="Book Search", bg="grey", command= lambda : booksearch.searchForBook(root))
    btn1.pack()
    btn2 = Button(root, text="Book Checkout", bg="grey", command= lambda : bookcheckout.AskIDs(root))
    btn2.pack()
    btn3 = Button(root, text="Book Return", bg="grey", command= lambda : bookreturn.returnBook(root))
    btn3.pack()
    btn4 = Button(root, text="Book List", bg="grey", command= lambda : booklist.GetPopularBooks(root))
    btn4.pack()
    btn5 = Button(root, text="Exit", bg="grey", fg="red", command=close_tk)
    btn5.pack()
    # The 'lambda' function allows parameters to be passed to a function when a button is clicked and stop it from
    # running instantly

    root.mainloop()

if __name__=="__main__":
    root = Tk()
    main()