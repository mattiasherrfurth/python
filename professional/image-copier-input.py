# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:22:07 2018

@author: J20032
"""

import os, shutil, datetime

currdir = input("What directory are we copying from?")
todir = input("What directory are we copying to?")

while os.path.exists(currdir)==False:
    currdir = input("Please enter a real filepath to copy from:")
    
if os.path.exists(todir)==False:
    resp = input("The directory to copy to does not exist. Do you want me to make one? (y/n)")
    if resp == 'y' or resp == 'Y':
        os.mkdir(todir)
        print('The directory %s has been created'%todir)
    elif resp == 'n' or resp == 'N':
        print('Okay then, I quit.')
    else:
        print('That response is not an option')

now = datetime.datetime.now().strftime('%Y%m%d%H%M')

testdir = r'C:\Users\J20032\Documents'

print('Looking for files in %s'%currdir)
print('\nMoving files to %s'%(r'C:\Users\J20032\Documents\images'+'\\'+now))

for subdirs, dirs, files in os.walk(currdir):
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif') or file.endswith('.bmp') or file.endswith('.jpeg'):
            shutil.copy2(subdirs+'\\'+file,todir)