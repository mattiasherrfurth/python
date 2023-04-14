#search_dir_for_str
#Purpose: Search a variety of files for specific strings
#Author: Mattias Herrfurth

import os, xlrd
from xlrd import open_workbook
search_path = input("Enter dir to search: ")

##returning all file types from directory
#make list of all files
file_list=[]
for dirpath, dir, files in os.walk(search_path):
    for file in files:
        file_list.append(file)
        
#function for checking if string has numbers
def hasNumbers(instring):
    return any(char.isdigit() for char in instring)

#return types of files in directory
file_types = []
for elem in file_list:
    elem = elem.split('.')
    type = elem[len(elem)-1]
    if type not in file_types and ' ' not in type and hasNumbers(type) == False:
        file_types.append(type)
print("These are your file type options: ", file_types)
print("Right now I can only read: ~nothing~")

#enter string to search for
search_str = input("Enter text to search for: ")

#append dir with '/' if not present
if not (search_path.endswith("/") or search_path.endswith("\\")):
    search_path = search_path + "/"

#if path doesn't exist, tell them that
if not os.path.exists(search_path):
    search_path = input("Enter a real directory to search: ")
    
for dirpath, dir, files in os.walk(search_path):
    for file in files:
        if file.split('.')[len(file.split('.'))-1]=="xlsm":
            print(file)
############## KEEP GOING ##############
    
    
######## EXTRA CODE ###########
    
##parse files in directory
#for fname in os.listdir(path=search_path):
#    fo = open(search_path + fname)
#    sd
#    line = fo.readline()
#    print('here')
#    line_no = 0
#    while line != '':
#        index = line.find(search_str)
#        if (index != -1):
#            print(fname, "[", line_no, ",", index, "]", line, sep="")
#        line = fo.readline()
#        line_no += 1
#    fo.close()
