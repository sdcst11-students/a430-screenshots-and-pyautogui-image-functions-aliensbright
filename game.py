#!python3
import time, pyautogui
import keyboard
'''
Main Task
Tap/hold the center of the planet repeatedly.

Task 1:
Every 1 minutes:
Click on the Increase damage button
Click on the Increase speed button
Click on the Increase limit button
Click on the Automation button

Task 2:
Every 3 minutes:
Click on the Collection button
Repeat until no gems visible and scrolled all the way down:
Scroll down until gems are visible or scrolled all the way down
Click on all gems
Click the ‘X’ at the bottom of the page

CRITERIA:
It should make use of functions and function calls to help break up your program into manageable tasks
It should incorporate a for loop
There should be a decision making process using if statements
A while loop should be incorporated to keep the program repeating
Use of a variables, including a list type variable must be part of your program.

'''

#setup: code on the right side of computer and game on the left side. 

planetCoords=[(350,450),(359,453),(362,456),(365,465),(362,474),(359,477),(350,480),(341,477),(338,474)(335,465),(338,456),(341,453)]
# (341,477) (338,474) (338,456) (341,453)
def setup():
    print('Here is the setup. You must have the program running\non the right side and the game running on the left side.')
    print('Once you have completed that,\nplease press the "s" key to start!')
    while True:
        if keyboard.is_pressed('s'):
            print('Thank you, we will now start the game.\nif at any time you would like to exit,\n just type "e"')
            break

def MainTask():
    pyautogui.mouseDown()
    for i in planetCoords:
        pyautogui.moveTo(i[0],i[1],0.5)
MainTask()
