#!python3
import pyautogui
import time
"""
locateImage Optional Parameters:

region: specifies a box (left, top, width,height) to search. This can signficantly speed up your search
"""

print('looking for icon on whole screen')
for i in range(10):
    start = time.time()
    x = pyautogui.locateCenterOnScreen('assets/winIcon.png')
    if x != None:
        # This is an important structure!
        # Sometimes you will look for an image and it will not be there
        # if you try to click on it, you will get an error because
        # None is not a tuple that is valid input for the pyautogui.click()
        # command
        print(round(time.time()-start,5),end=", ")
pyautogui.moveTo(1100,250)
print('\n\nlooking in a small box on the bottom left (note that your screen is 1440x900)')
for i in range(10):
    start = time.time()
    x = pyautogui.locateCenterOnScreen('assets/winIcon.png',region=(1100,250,100,100) )
    print(round(time.time()-start,5),end=", ")
