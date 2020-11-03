import pyautogui
import time

checkTime = 5 * 60

def moveMouse():
    pyautogui.moveTo(500, 500, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(600, 500, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(600, 600, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(500, 600, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(600, 500, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(600, 600, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(500, 600, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(500, 600, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(500, 500, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(600, 800, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(200, 600, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(900, 100, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(500, 400, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(100, 900, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(600, 300, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(500, 600, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(600, 500, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(600, 600, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(500, 900, duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(900, 200, duration=0.1, tween=pyautogui.easeInOutQuad)

def main():
    count = 0
    while(True):
        posX, posY = pyautogui.position()
        time.sleep(1)
        nposX, nposY = pyautogui.position()
        if posX == nposX and posY == nposY:
            count += 1
        else:
            count = 0
        if(count == checkTime):
            moveMouse()
            count = 0

main()
