# Локальная первичная обработка строк
from collections import deque
from config import categories, yt_categories
from utils import logger
def classify(title, process_name):
    category_result = {}
    process_lower = process_name.lower()
    title_lower = title.lower()
        # --- ЛОГИКА ДЛЯ YOUTUBE ---    
    if "youtube" in title_lower: 
        for cat_name , cat_data in yt_categories.items():
            current_score = 0 
            weight = cat_data.get("weights", {})

            for word, value in weight.items(): 
                if word in title_lower:
                    current_score += value
            if current_score > 0: 
                category_result[cat_name] = current_score
        if not category_result: 
            return "Unknow Youtube content"
        winner = max(category_result, key=category_result.get)
        return winner
    
        # ---  ЛОГИКА ДЛЯ FIREFOX (НЕ YOUTUBE) ---
    if process_lower == "firefox.exe":
        for cat_name, cat_data in categories.items(): 
            keywords = cat_data.get("keywords", [])
            if isinstance(keywords,str): keywords = [keywords]

            for word in keywords:
                if word.lower() in title_lower: 
                    return cat_name
        return "Unknows category"
            
    # ---  ЛОГИКА ДЛЯ ОСТАЛЬНЫХ ПРОЦЕССОВ ---
    for cat_name, cat_data in categories.items(): 
        processes_list = cat_data.get("processes", [])
            
        if process_lower in [p.lower() for p in processes_list if isinstance(p, str)]:
            return cat_name
    return "Unknows System Process"



    # with open(file=r'C:\Users\manyt\Desktop\Time-tracker\Auto-Time-Tracker\logs\logs.log', mode="r", encoding="UTF-8") as f: 
    #     last_line = deque(f,maxlen=1) # читаем последнюю
    #     print(last_line[0].strip('\n'))
    # # return "Классификия" 
