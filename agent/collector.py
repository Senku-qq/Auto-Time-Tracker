# Логика захвата окон (pywin32)
import win32gui
import time 

def test(): 
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    print(title)

if __name__ == "__main__":
    time.sleep(3)
    test() 
