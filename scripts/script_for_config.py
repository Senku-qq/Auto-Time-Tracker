data = []
with open(file=r"C:\Users\manyt\Desktop\Time-tracker\Auto-Time-Tracker\scripts\data.txt",mode="r", encoding="UTF-8") as f: 
    line = f.readlines()
    for l in line:
        data.append(l.strip("\n"))

print(data)