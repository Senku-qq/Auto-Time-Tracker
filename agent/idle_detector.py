# Логика pynput
from pynput import keyboard , mouse
import time 
class IdleDetector: 
    def __init__(self, threshold=10):
        self.threshold = threshold
        self.last_input_time = time.time()

        self.mouse_listener = mouse.Listener(on_move=self.on_activity, on_click=self.on_activity , on_scroll=self.on_activity)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_activity, on_release=self.on_activity)

        self.mouse_listener.start()
        self.keyboard_listener.start()

    def on_activity(self, *args) -> int: 
        self.last_input_time = time.time()
    
    def last_activity_time(self) -> int:
        return time.time() - self.last_input_time 
    
    def is_idle(self) -> bool: # если пользователь долго не двигается то отключаем сбор 
        return self.last_activity_time() > self.threshold
    
# detector = IdleDetector()
# print(detector.last_activity_time())
# print(detector.is_idle())
