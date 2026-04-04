# Логика захвата окон (pywin32)
import win32gui
import win32process
import psutil
import time 
import logging
from colorama import  Fore , Back , Style  

# from classifier import get_class
class Collector:
    def __init__(self):
        self.active_window= { 
                "monitor": int, 
                "title": list,
                "process_name": str, 
                "x_cord": int,
                "class": str, 
            }
    #LOGGING
    logging.basicConfig(
    filename=r"C:\Users\manyt\Desktop\Time-tracker\Auto-Time-Tracker\logs\logs.log",
    encoding="UTF-8",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    )
    logger = logging.getLogger(__name__)  
    
    def get_monitors_activity(self) -> dict:
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
        
        # category = get_class(process_name, title)
        # вызываем функцию классификации, получаем класифицированную информацию и отправляем её в бд 
        #передавать туда просто стринг и результат функции записывать уже тут в active window 
        # category = Classifier.get_class(string) "category": category
        
        self.active_window = { 
            "monitor": monitor, 
            "title": title[0] if title else "Untitled Window",
            "process_name": process_name, 
            "x_cord": x_left,
            # "category": category
        }
        # вызываем функцию классификации, получаем класифицированную информацию и отправляем её в бд 
        self.logger.info(f"Current window: {[self.active_window]} ")
        return  [self.active_window] # данные должны отсуда идти в бд 

if __name__ == "__main__":
    collector = Collector()
    time.sleep(3)
    print(collector.get_monitors_activity())


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