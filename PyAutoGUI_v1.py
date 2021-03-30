# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:38:32 2019

@author: J20032
"""

import pyautogui

pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

def AltTab():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')

def SAP_TabTwice():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('pagedown')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('pagedown')




def main():
    AltTab()
    SAP_TabTwice()

main()