def GetDataFromFile():
    """This function retrieves all of the details on books stored in database.txt and saves it in the variable data
    """
    data = []
    DataFile = open('database.txt', mode='r')
    for line in DataFile:
        data.append((line.rstrip('\n')).split('  '))
    # Reads in each line of database.txt to the list, data, and splits it up when two spaces occur
    DataFile.close()
    return data

def WriteToFile(data):
    """This function writes everything stored in the variable data into database.txt

    Parameters: data - contains all of the book details
    """
    file = open('database.txt', mode='w')
    data1 =[]
    for i in data:
        x = '  '.join(i)
        data1.append(x)
    for book in data1:
        file.writelines(book + "\n")
    # Joins each element of each sublist with a double space in between then then writes it to database.txt with a new
    # line in between each element
    file.close()

def GetDataFromLogfile():
    """This function retrieves all of the details on books withdrawals stored in logfile.txt and saves it in the
    variable data
    """
    data = []
    DataFile = open('logfile.txt', mode='r')
    for line in DataFile:
        data.append((line.rstrip('\n')).split('  '))
    DataFile.close()
    return data

def WriteToLogfile(data):
    """This function writes everything stored in the variable data into logfile.txt

    Parameters: data - contains all of the book withdrawal details
    """
    file = open('logfile.txt', mode='w')
    data1 =[]
    for i in data:
        x = '  '.join(i)
        data1.append(x)
    for book in data1:
        file.writelines(book + "\n")
    file.close()

if __name__ =="__main__":
    # Testing GetDataFromFile and GetDataFromLogfile
    GetDataFromFile()
    GetDataFromLogfile()
    # Testing WriteToFile and WriteToLogfile (Will edit database.txt and logfile.txt)
    WriteToFile(["11", "Harry Potter", "J. K. Rowling", "10/10/2019", "0"])
    WriteToLogfile(["11", "12/10/2019", "14/10/2019"])
