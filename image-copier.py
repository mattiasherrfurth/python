# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:25:06 2018

@author: J20032
"""

import os, shutil, datetime

#currdir = os.getcwd()
currdir = r'T:\A\AMEC\Quality Engineering'
now = datetime.datetime.now().strftime('%Y%m%d%H%M')
todir = r'C:\Users\J20032\Documents\IMAGE_OUTPUT\images_'+now

testdir = r'C:\Users\J20032\Documents'

print('Looking for files in %s'%currdir)
print('\nMoving files to %s'%(r'C:\Users\J20032\Documents\images'+'\\'+now))

for subdirs, dirs, files in os.walk(currdir):
    for file in files:
        if os.path.exists(todir)==False:
            os.mkdir(todir)
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif') or file.endswith('.bmp'):
            shutil.copy2(subdirs+'\\'+file,todir)