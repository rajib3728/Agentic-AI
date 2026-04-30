import pyautogui
import time
time.sleep(5)

# returns a point 
#  object with 
# x and y values
print(pyautogui.position()) 
x,y=pyautogui.position()
print(int(x)*5,int(y))