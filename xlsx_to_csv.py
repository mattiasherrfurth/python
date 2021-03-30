import xlrd
import csv
import os

def csv_from_excel():
    #ask for excel filepath
    book = input("Input path for excel book: ")
    #check for if it exists, request a real path
    while not os.path.exists(book):
        book = input("Enter a real book: ")
    #create folder location variable
    print(book)
    dir_list = book.split('\\')
    file_name = dir_list[len(dir_list)-1].split('.')[0]
    print(file_name)
    dir = ''
    n = 0
    while n+1 < len(dir_list):
        dir = dir + dir_list[n] + '\\'
        n += 1
    
    wb = xlrd.open_workbook(book)
    sh = wb.sheet_by_name('Sheet1')
    csv_file = open('%s.csv' %file_name,  'wb')
    wr = csv.writer(csv_file,  quoting = csv.QUOTE_ALL)
    for rownum in range(sh.nrows):
        #####CAN'T HANDLE TEXT#########
        wr.writerow(sh.row_values(rownum))
    csv_file.close()


csv_from_excel()
