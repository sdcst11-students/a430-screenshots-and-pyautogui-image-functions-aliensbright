import pyautogui


x = pyautogui.pixel(100,200)
print(f"The color of the pixel at (100,200) is {x}")
print("This tells us the amount of red, green and blue")

if pyautogui.pixelMatchesColor(100,200,x, tolerance=0.9):
    print("we had a pixel match!")

if pyautogui.pixelMatchesColor(200,200,(52,52,49), tolerance=0.9):
    print("we had a pixel match!") 
else:
    print('the second pixel did not match')

