'''
Jeremy Johnson
CYBR410
Assignment 6.2
7/6/2022
'''

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vj6wlif.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for i in docs: 
    print('Student ID: ' + i['student_id'] + '\n' + 'First Name: ' + i['first_name'] + '\n' + 'Last Name: ' + i['last_name'] + '\n')

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")

change = db.students.update_one({"student_id": '1007'}, {"$set": {"last_name": "Bear"}})
result = db.students.find_one({"student_id" : '1007'})

(print('Student ID: ' + result['student_id'] + '\n' + 'First Name: ' + result['first_name'] + '\n' + 'Last Name: ' + result['last_name'] + '\n'))
