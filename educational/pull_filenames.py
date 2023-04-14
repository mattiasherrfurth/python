import os

search_path = input("Enter dir to search: ")

#want to see if the path actually exists before attempting to search through it
if not os.path.exists(search_path):
    search_path = input("Enter a real directory to search: ")

#want to compile a list of all the filenames in the directory
file_list=[]
for dirpath, dir, files in os.walk(search_path):
    for file in files:
        file_list.append(file)
