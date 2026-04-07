# Локальная первичная обработка строк
from collections import deque
def classified():
    with open(file=r'C:\Users\manyt\Desktop\Time-tracker\Auto-Time-Tracker\logs\logs.log', mode="r", encoding="UTF-8") as f: 
        last_line = deque(f,maxlen=1) # читаем послеюнюю
        print(last_line[0].strip('\n'))
classified()