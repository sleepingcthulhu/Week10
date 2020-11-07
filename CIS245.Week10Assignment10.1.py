'''
Brad Fogarty
CIS245: Introduction to Programming
Bellevue University
Professor Jordan Moline
November 9th, 2020

Instructions:
This week we will create a program that performs file processing activities.
Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
The program should then prompt the user for their name, address, and phone number.  Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.

Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes.

Submit a link to your Github repository.'''
import os

class User(object):
    def __init__(self, name, address, phone, fileLocation):
        self.name       = name
        self.address    = address
        self.phone      = phone
        self.fileLocation    = fileLocation

    def display(self):
        #READ FROM FILE
        print(f"Reading from {self.fileLocation} :")
        with open(f'{self.fileLocation}') as file:
            for line in file:
                print(f"\t{line}")

    def write(self):
        #WRITE DATA TO NEW FILE
        with open(f'{self.fileLocation}', 'w') as file:
            file.write(f'{self.name}, {self.address}, {self.phone}')

    def append(self):
        #APPEND DATA TO EXISTING FILE
        with open(f'{self.fileLocation}', 'a') as file:
            file.write(f'\n{self.name}, {self.address}, {self.phone}')

def getPath():
    filepath = str(input("Enter directory: "))
    if os.path.isdir(filepath):
        print("Directory exists")
        makeFile(filepath)
    else:
        print(f"Directory {filepath} does not exist")
        getPath()

def makeFile(filepath):
    filename = str(input("Enter filename, do not forget file extension!: "))
    fileLocation = os.path.join(filepath, filename)
    #FILENAME FOUND:
    if os.path.isfile(fileLocation):
        userChoice = str(input(f"file {filename} already exists, do you want to modify this file?\ny/n:  "))
        if userChoice == 'y' or 'yes':
            #APPEND FILE
            appendUser(fileLocation)
        elif userChoice == 'n' or 'no':
            print("choose another filename")
        else:
            print("enter something logical ya dingus.")
    #FILENAME NOT FOUND:
    if not os.path.isfile(fileLocation):
        #CREATE NEW FILE
        writeUser(fileLocation)


def writeUser(fileLocation):
    name    = str(input('Enter name: '))
    address = input('Enter address: ')
    phone   = int(input('Enter phonenumber: '))
    user = User(name, address, phone, fileLocation)
    user.write()
    user.display()

def appendUser(fileLocation):
    name    = str(input('Enter name: '))
    address = input('Enter address: ')
    phone   = int(input('Enter phonenumber: '))
    user = User(name, address, phone, fileLocation)
    user.append()
    user.display()


if __name__ == '__main__':
    getPath()
