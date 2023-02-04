# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile_ao = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile_ao.name)
print('Is Closed : ', myFile_ao.closed)
print('Opening Mode: ', myFile_ao.mode)

# Write to file
myFile_ao.write('I love Python')
myFile_ao.write(' and C#')
myFile_ao.close()

# Append to file
myFile_ao = open('myfile.txt', 'a')
myFile_ao.write(' I hate PHP')
myFile_ao.close()

# Read from file
myFile_ao = open('myfile.txt', 'r+')
text = myFile_ao.read(100)
print(text)