'''
Jeremy Johnson
CYBR410
Assignment 5.3
6/28/2022
'''

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vj6wlif.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech


fred = {
    "student_id" : "1007",
    "first_name" : "Fred",
    "last_name" : "Willard"
    
}

mary = {
    "student_id" : "1008",
    "first_name" : "Mary",
    "last_name" : "Poppins"
}

steve = {
    "student_id" : "1009",
    "first_name" : "Steve",
    "last_name" : "Perry"
}

fred_student_id = db.students.insert_one(fred).inserted_id
mary_student_id = db.students.insert_one(mary).inserted_id
steve_student_id = db.students.insert_one(steve).inserted_id

print("-- INSERT STATEMENTS --")
print("Inserted student record Fred Willard into the students collection with document id {}".format(fred_student_id))
print("Inserted student record Mary Poppins into the students collection with document id {}".format(mary_student_id))
print("Inserted student record Steve Perry into the students collection with document id {}".format(steve_student_id))
