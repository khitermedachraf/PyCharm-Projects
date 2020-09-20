# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

path = "C:\\Users\\TRETEC\\Desktop\\KHITER Med Achraf"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def listDir(dir) :
    fileNames = os.listdir(dir)
    for fileName in fileNames :
        print("File name : " + fileName)
        print("Folder path : " + os.path.abspath(os.path.join(dir,fileName)) + "\n")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 print_hi('KHITER Med Achraf')

result = os.listdir(path)
for x in result:
    print(x)
print("hhhhhhhhhhhhhhhhh\n\n")

listDir(path)
# verify if a the object is a directory or file with (isdir,isfile)
print("is it a directory ? \n"+ path + "\n")
print(os.path.isdir(path))

pathFile ="D:\\Mon travail\\Git & Github\\Pycharm Projects\\PyCharm-Projects\\first project\\main.py"

print("is it a file ? \n"+ pathFile + "\n")
print(os.path.isfile(pathFile))

