import pyautogui
import time


print(" _______    _______           _        ____  _____   ___  ____       _______  ____  ____")
print("|_   __ \  |_   __ \         / \      |_   \|_   _| |_  ||_  _|     |_   __ \|_  _||_  _|")
print("  | |__) |   | |__) |       / _ \       |   \ | |     | |_/ /         | |__) | \ \  / /")
print("  |  ___/    |  __ /       / ___ \      | |\ \| |     |  __'.         |  ___/   \ \/ /")
print(" _| |_      _| |  \ \_   _/ /   \ \_   _| |_\   |_   _| |  \ \_   _  _| |_      _|  |_  ")
print("|_____|    |____| |___| |____| |____| |_____|\____| |____||____| (_)|_____|    |______|   ")
time.sleep(1)
print("Your screen size \/ ")
time.sleep(0.5)
print(pyautogui.size())
time.sleep(1)

print("Prank list:")
time.sleep(0.5)
print("[1] Mouse Interrupter")
print("[2] Screen Interrupter")
print("[3] Keyboard Interrupter")
time.sleep(1)

option = input("!!! Type the number you want to activate -->: ")


if option == "1":
    num1 = 1000
    num1cur = 1
    print("Mouse Interruptor Selected")
    print("Starting...")

    while num1cur != num1:
        time.sleep(3)
        pyautogui.moveRel(0, 100, duration=0.1)
        pyautogui.moveRel(0, -100, duration=0.1)
        pyautogui.moveRel(500, 0, duration=0.1)
        pyautogui.moveRel(-500, 0, duration=0.1)

elif option == "2":
    num2 = 1000
    num2cur = 1
    print("Screen Interruptor Selected")
    print("Starting...")
    while num2cur != num2:
        time.sleep(60)
        pyautogui.click(10, 10)
        pyautogui.click(20,265)

elif option == "3":
    num3 = 1000
    num3cur = 1
    print("Keyboard Interruptor Selected")
    print("Starting...")
    while num3cur != num3:
        time.sleep(10)
        pyautogui.typewrite("Asd")
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.hotkey( "command", "f")
