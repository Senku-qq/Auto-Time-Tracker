# Точка входа в агент
# идеи : Вызывать collector() тут, каждые 5 секунд 
# Также тут должны вызываться все функции, надо написать тестовые вызовы чтобы проверить совместимость коллектора с детектора
from collector import * 
from idle_detector import * 
from flask import Flask, request
import threading
import time 
detector = IdleDetector()
collector = Collector()
is_already_idle = False

app = Flask(__name__)
# Здесь будем хранить последние данные из браузера
web_context = {"url": "", "title": "", "channel": ""}

@app.route('/track', methods=['POST'])
def track():
    global web_context
    web_context = request.json
    return {"status": "received"}

def start_api():
    # Запуск без лишнего спама в консоль
    app.run(port=5000, debug=False, use_reloader=False)

threading.Thread(target=start_api, daemon=True).start()

while True:
    if detector.is_idle(): # если нет движения то входим в цикл ожилания какого то действия 
        if is_already_idle:
            time.sleep(5)
            continue
        else:
            is_already_idle = True
            print("Система в режиме ожидания любого действия...")
            continue

    try: 
        is_already_idle = False
        data = collector.get_monitors_activity()
        print(f"Активность:{data}")

    except Exception as e: 
        print(f"Error: {e}")
    time.sleep(5)
