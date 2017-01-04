import pyautogui
import time
import random

def getmouseposition():
	xmouse, ymouse = pyautogui.position()
	return xmouse, ymouse

def movemouse(screendef):
	newmouse = []
	newmouse.append(random.randint(0,screendef[0]))
	#y coordinate minus 200 so the mouse doesnt pop up a window (annoying)
	newmouse.append(random.randint(0,screendef[1]-200))
	pyautogui.moveTo(newmouse[0], newmouse[1], duration=1)

timeout = 3
nowmouse = []
lastmouse = []
nowmouse = getmouseposition()
lastmouse = nowmouse
inactive = 0

while True:
	time.sleep(1)
	nowmouse = getmouseposition()
	if nowmouse[0] == lastmouse[0]:
		inactive += 1
		print('inactive')
		if inactive > timeout:
			inactive = 0
			screen = []
			screen = pyautogui.size() 
			movemouse(screen)
	else:
		print('active')
		nowmouse = getmouseposition()
		lastmouse = nowmouse
		inactive = 0




