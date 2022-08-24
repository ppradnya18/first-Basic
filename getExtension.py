"""Write a Python program to accept a filename from the user and print the extension of that. """


getFilename=input("Enter name of file to get the extension ")

sdd=getFilename.split(".")

print("The extension of file is ",sdd[-1])

