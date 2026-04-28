# Настройки (интервал проверки, URL бэкенда)
yt_categories = {
    "learning": {
        "weights": {   
            "python": 35,
            "javascript": 35,
            "backend": 35, 
            "frontend": 35, 
            "coding": 30, 
            "разработка": 30,
            "скрипт": 30,
            
            "курс": 30,
            "tutorial": 28, 
            "урок": 28,
            "обучение": 25, 
            "с нуля": 25,

            "математика": 25,
            "math": 20,

            "docker": 18,
            "metanit": 20,

            "как": 5, 
            "гайд": 8,
            "за": 1
        },
    },
    "games": {
        "weights": {
            "cs2": 35,
            "dota": 35,
            "rust": 35,

            "gameplay": 25,
            "прохождение": 30,
            "стрим": 25,
            "let’s play": 30,

            "раст": 20,
            "boss": 10
        },
    },
    "history": {
        "weights": { 
            "история": 35,
            "рим": 30,
            "ссср": 30,
            "ww2": 30,

            "древний": 25,
            "империя": 22
        },
    },
    "politics": { 
        "weights": {
            "путин": 30,
            "трамп": 30,
            "зеленский": 30,

            "война": 25,
            "russia": 20,
            "ukraine": 20
        },
    },
    
    "music": {
        "weights": {
            "музыка": 30,
            "music": 30,

            "lofi": 25,
            "chill": 20,
            "relax": 20,

            "playlist": 15
        },
    },
    "coding": {
        "weights": {
            "leetcode":6,
            "python":8,
            "javascript":6,
            "coding":27,
            "разработка":17,
            "backend":18,
            "frontend":8,
            "php":5,
            "cpp":7,
            "c++":29,
        },
        
    }
}

categories = {
    "anime": {
        "processes": ["firefox.exe"],
        "keywords": "YummyAnime"
        },
    "communication": {
        "processes": ["discord.exe","telegram.exe"],
        },
    "coding": {
        "processes":["code.exe", "git-bash.exe","godot-engine.exe", "docker-desktop.exe"],
        }, 
    "games": {
        "processes": ["rust.exe","cs2.exe","pubg.exe","dota.exe","raft.exe","civilizationIV.exe","valorant.exe","osu.exe","7daystodie.exe","tlauncher.exe"]
        }, 
    "steam": {
        "processes": ["steam.exe"]
        },
    "art": {
        "processes": ["photoshop.exe","powerpoint.exe", "paint.exe", "blender.exe","capcut.exe"],
        },
    "notes": {
        "processes": ["obsidian.exe"]
        },
    "learning": {
        "processes": ["packettracer.exe", "LauncherPatcher.exe","VirtualBox.exe"]
        }
}

