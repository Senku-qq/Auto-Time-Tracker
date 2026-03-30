# Логика pynput
from pynput import keyboard , mouse
import time 
class IdleDetector: 
    def __init__(self, threshold=120):
        self.threshold = threshold
        self.last_input_time = time.time()

        self.mouse_listener = mouse.Listener(on_move=self.on_activity, on_click=self.on_activity , on_scroll=self.on_activity)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_activity, on_release=self.on_activity)

        self.mouse_listener.start()
        self.keyboard_listener.start()

    def on_activity(self): 
        self.last_input_time = time.time()
    
    def last_activity_time(self):
        return time.time() - self.last_input_time 
    
    def is_idle(self): # если пользователь долго не двигается то отключаем сбор 
        return self.last_activity_time() > self.threshold
    

    # надо будет сделать проверку на то, открыт ли сейчас плеер ютуб или что то где не нужна мышь и клавиатура 