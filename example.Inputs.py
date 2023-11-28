import pyautogui

x = pyautogui.alert("This is an alert box!  Does nothing, but could pause your program")

y = pyautogui.prompt("This is a prompt! It allows you to store a value, just like the input command")
print(f"You entered a {y}")


