

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
#firebase_admin.initialize_app(cred)



firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://attendanceprojectfr-default-rtdb.firebaseio.com/"
    },
)

ref = db.reference("Students")


data = {
    "TP011111": {
        "name": "Lee Wen Han",
        "major": "CS(AI)",
        "starting_year": 2021,
        "total_attendance": 20,
        "grades": "A",
        "year": 2,
        "last_attendance_taken": "2024-01-26 16:10:30",
    },
    "TP054321": {

        "name" : "Elon Musk",
        "major" : "Ruining Lives",
        "starting_year": 2020,
        "total_attendance": 100,
        "grades" : "A+",
        "year" : 4,
        "last_attendance_taken" : "2024-01-22 01:30:30",},

    "TP063338": {

        "name" : "Dalton Gan",
        "major" : "SE",
        "starting_year": 2020,
        "total_attendance": 64,
        "grades" : "A+",
        "year" : 2,
        "last_attendance_taken" : "2024-01-22 01:30:30",},

    "TP068713": {

        "name" : "Suzanne Lai",
        "major" : "CS(AI)",
        "starting_year": 2021,
        "total_attendance": 10,
        "grades" : "A+",
        "year" : 2,
        "last_attendance_taken" : "2024-01-22 01:30:30",},

    "TP066765": {

        "name" : "Nikitha Upadhya",
        "major" : "SE",
        "starting_year": 2021,
        "total_attendance": 1,
        "grades" : "A+",
        "year" : 3,
        "last_attendance_taken" : "2024-01-22 01:30:30",},



    
}

for key, value in data.items():
    ref.child(key).set(value)