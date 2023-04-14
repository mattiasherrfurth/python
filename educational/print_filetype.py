import os

search_path = input("Enter dir to search: ")

#check if path exists
if not os.path.exists(search_path):
    search_path = input("Enter a real directory to search: ")

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
print("These are your options for file types: ", file_types)

input("All good?")
