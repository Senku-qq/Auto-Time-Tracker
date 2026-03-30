# Логика захвата окон (pywin32)
import win32gui
import win32process
import psutil
import time 


def get_monitors_activity():
    # Надо сделать красивее
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd).splitlines("-")
    pid = win32process.GetWindowThreadProcessId(hwnd) #Тут выподиться так (ID потока, ID процесса) нам нужен id процесса 
    rect = win32gui.GetWindowRect(hwnd)
    process_name = psutil.Process(pid[1]).name()
    x_left = rect[0]

    if -10 <= x_left < 1900: 
        monitor = 1
    elif x_left >= 1900: 
        monitor = 2
    else: return "Error: Unknown monitor"     

    active_window = { 
        "monitor": monitor, 
        "title": title[0],
        "process_name": process_name, 
        "x_cord": x_left
    }
    return  [active_window]

if __name__ == "__main__":
    time.sleep(3)
    print(get_monitors_activity())


# callback beta for future 
    # def enum_callback(self, hwnd): 
    #     if win32gui.IsWindowVisible(hwnd):
    #         title = win32gui.GetWindowText(hwnd)
    #         if title: 
    #             rect = win32gui.GetWindowRect(hwnd)
                
    #             x_left = rect[0]
                
    #             if x_left <= -32000: # определяем свернутые окна  
    #                 return 
    #             if 0 <= x_left < 1920: 
    #                 self.monitor = 1 
    #             elif x_left > 1920: 
    #                 self.monitor = 2 
    #             else: 
    #                 return "Error: Unknown monitor"