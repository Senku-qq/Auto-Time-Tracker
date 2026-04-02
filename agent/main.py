# Точка входа в агент
# идеи : Вызывать collector() тут, каждые 5 секунд 
# Также тут должны вызываться все функции, надо написать тестовые вызовы чтобы проверить совместимость коллектора с детектора
from collector import * 
from idle_detector import * 
import time 

detector = IdleDetector()
while True:
    if detector.is_idle(): # если нет движения то входим в цикл ожилания какого то действия 
        print("Система в режиме ожидания любого действия...")
        time.sleep(5)
        continue

    try: 
        data = get_monitors_activity()
        print(f"Активность:{data}")

    except Exception as e: 
        print(f"Error: {e}")
    time.sleep(5)