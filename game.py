#!python3
import time, pyautogui
import keyboard
from pyscreeze import locate
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
# (341,477) (338,474) (338,456) (341,453)
def setup():
    print('Here is the setup. You must have the program running\non half the screen, and the game on the other side left.')
    print('Once you have completed that,\nplease press the "s" key to start!')
    while True:
        if keyboard.is_pressed('s'):
            print('Thank you, we will now start the game.\nif at any time you would like to exit,\n just type "e"')
            break

def MainTask():#350,465
    x,y=pyautogui.locateCenterOnScreen('assets/collection.png', confidence=.7)
    pyautogui.moveTo(x,y)
    print(pyautogui.locateCenterOnScreen('assets/collection.png',confidence=0.6))
    x=x+144
    y=y+106
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown()
    return x,y
    
def start(): #gets to the main screen
    try:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/rungame.png'))
        pyautogui.click(clicks=2,interval=0.5)
        time.sleep(3)
    except:
        try:
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/sleep.png',confidence=0.8))
            pyautogui.click(clicks=2,interval=0.5)
            time.sleep(1)
        except:
            pass


def sidetask1(): #goes to the shop on the bottom of the screen.
    n=True
    shoplist=['damage','speed','limit','auto']
    while n==True:
        for i in shoplist:
            try:
                pyautogui.moveTo(pyautogui.locateCenterOnScreen(f'assets/{i}.png',confidence=0.9))
                mousething()          
            except:
                if i=='auto':
                    n=False

def sidetask2(): #Go into rebirth tab and use feathers for effects
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/rebirth.png',confidence=0.9))
    pyautogui.click(clicks=2,duration=0.5)
    x,y= pyautogui.locateCenterOnScreen('assets/rebirthknife.png',confidence=0.9)
    reCoords=[(x,y),(x+75,y),(x+150,y),(x+225,y),(x,y+100),(x+75,y+100),(x+150,y+100),(x+225,y+100)]
    for i in reCoords:
        pyautogui.moveTo(i[0],i[1],0.1)
        pyautogui.click()
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/xmarks.png',confidence=0.9))
    pyautogui.click(2,duration=0.5)


def sidetask3(a,b): #collects gems from the collection tab
    x,y=(pyautogui.locateCenterOnScreen('assets/collection.png', confidence=.7))
    pyautogui.moveTo(x,y-20)
    mousething()
    mousething()
    for i in range(4):
        while True:
            try:
                pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/gems.png',region=(x,y-100,300,500),confidence=0.9))
                pyautogui.click(clicks=2,duration=0.2)
            except:
                break
        pyautogui.moveTo(a,b+180)
        pyautogui.mouseDown()
        pyautogui.moveTo(a,b-190,1)
        pyautogui.mouseUp()   
        time.sleep(1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/xmarks.png',confidence=0.9))
    pyautogui.click(2,duration=0.5)
    


def mousething():
    pyautogui.mouseDown()
    pyautogui.mouseUp()

start()
x,y = MainTask()
#sidetask1()
#sidetask3(x,y)
sidetask2()