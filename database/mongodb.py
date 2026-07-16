from pymongo import MongoClient

try:
    MONGO_URI = "mongodb+srv://monikalowanshi90_db_user:monika123@cluster0.vsf713q.mongodb.net/?appName=Cluster0"

    client = MongoClient(MONGO_URI)

    client.andmin.command("ping")
    
    db = client["ssus"]
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_report"]

    print("MongoDB connected Successfully!")
except Exception as e:
    print("MongoDB error:",e)