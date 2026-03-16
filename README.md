# Digital-Hunter
Final Exam Day 1
Yehuda Freiman 205368319 Arava


## תיאור
המערכת מאזינה לקפקא עושה אנליזה ושומרת במונגו

## ארכיטקטורה


## דרישות מקדימות
- Docker + Docker Compose
- Python 3.10+
- Git

## הרצה מקומית

```bash
# 1. שכפל את הריפו
git clone https://github.com/yehudafreiman/Digital-Hunter.git
cd DigitalHunter
# 3. הרץ את כל השירותים
docker-compose up --build
```

## משתני סביבה
הגדר קובץ `.env` בתיקייה הראשית:
```env
KAFKA_BROKER=kafka:9092
ES_HOST=http://elasticsearch:9200
MONGO_URI=mongodb://mongodb:27017
```

## מבנה הפרויקט
````
├── README.md
├── analyze
│   ├── Dockerfile
│   ├── analyze.py
│   └── requirements.txt
├── consumer
│   ├── Dockerfile
│   ├── consumer.py
│   └── requirements.txt
├── docker-compose.yml
├── haversine.py
├── loader
│   ├── Dockerfile
│   ├── loader.py
│   └── requirements.txt
├── shared
│   ├── __init__.py
│   ├── connection.py
│   └── logger.py
├── students_part_1
│   ├── README.md
│   ├── requirements.txt
│   └── simulator.py
└── test
    ├── README.md
    ├── docker-compose.yaml
    ├── producer.py
    └── tracker.py

