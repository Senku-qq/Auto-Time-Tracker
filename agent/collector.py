# Логика захвата окон (pywin32)
import win32gui
import time 



def get_monitors_activity():

    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    active_window = { 
        "monitor": 1, 
        "title": title, 
        "is_main": True 
    }
    return  [active_window]

if __name__ == "__main__":
    time.sleep(3)
    print(get_monitors_activity())

