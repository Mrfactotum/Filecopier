README for Filecopier.py

Summary:

File copier is a small program written in Python 3 which allows you 
to transfer certain file extensions from a tree of folders and 
subdirectories to a destination folder.

Dependencies:

Filecopier uses the following modules that come with Python 3:
os
shutil

What can I use it for? 

Imagine you have hundreds of excel files mixed in with word documents,
photos and other files nested in many folders. This program allows you
to search through a directory tree and pull out all the files ending 
with a certain file name.



Usage Example:
Open filecopier in a text editor
Edit the following lines:

#replace "(/source-directory/") with the parent folder you want to copy from.
source_directory = ("source-directory")

#replace "destination-directory"  with the path to your destination
destination_directory = ("destination-directory")

#Replace ('.txt') in if f.endswith('.txt')
#with the file ending of your choice.
if f.endswith('.txt'):

Run the program

LICENSING:
This program is distrubted with an MIT License the full text of which can
be found under the License document.

December 2017
