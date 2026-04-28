import random
data = []
def keywords():
    with open(file=r"C:\Users\manyt\Desktop\Time-tracker\Auto-Time-Tracker\scripts\data.txt",mode="r", encoding="UTF-8") as f: 
        line = f.readlines()
        for l in line:
            data.append(l.strip("\n"))
def weights(text):
    for i in text:
        print(f'"{i}":{random.randint(5,30)},')

print(weights(["leetcode","python", "javascript", "coding","разработка", "backend", "frontend", "php", "cpp", "c++"]))
