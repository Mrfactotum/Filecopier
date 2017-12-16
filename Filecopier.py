#Copy files with a certain ending from inside a tree of folders to another
#destination.

import shutil
import os

#replace "(/source-directory/") with the parent folder you want to copy from.
source_directory = ("source-directory")

#replace "destination-directory"  with the path to your destination
destination_directory = ("destination-directory")

def copyFiles():
#Find and copy files with a certain ending 
#Replace ('.txt') in if f.endswith('.txt')
#with the file ending of your choice.
	for root, directory, files in os.walk(source_directory):
		for f in files:
			if f.endswith('.txt'):
				print("Copying: " + f)
				shutil.copy(os.path.join(root, f), destination_directory)
		
copyFiles()			
