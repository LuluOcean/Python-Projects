#!/usr/bin/python3
import os

# This code allows you to enter and list contents of any directory, given user have permission to view the directory.
# script does not open or reads any files

#Prints and lists current directory and its contents
def DirPath():
    print("\n\n\t\tCurrent Dicretory:\n>",os.getcwd())
   

#Presents contents as a list to choose from    
DirList = list()
def DirOption():
    DirPath()
    print("\n\tCurrent Directory contents listed as options below:")
    for Content in os.listdir():                    # os.listdir() built-in function to list contents in a diretory
        DirList.append(Content)
    for option in range(len(DirList)):
        print(f"\n> Option {option}: ", end=' ')
        os.system(f"file {DirList[option]}")        # word "file" is used to tell us what type is it that specific file


#This function changes directories
def DirChange():
    choice = int(input("""\nEnter an option number to open a file or enter into a directory.
                       Or enter 619 to go back a directory:\n> """))
    if choice != 619:
        os.chdir(f"./{DirList[choice]}")   # Changes the directory using "os.chdir"
        main()
    else:
        os.chdir("./..")
        main() 


def main(): 
    for _ in range(len(DirList)):       #This loop clears the DirList of its content
        DirList.remove(DirList[0])       
    DirOption()
    DirChange()
    
main()
