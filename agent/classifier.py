# Локальная первичная обработка строк

def classified():
    with open(file='/logs/logs.log', mode="r", encoding="UTF-8") as f: 
        f.readline() # читать надо снизу
        
