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
docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for i in docs: 
    print('Student ID: ' + i['student_id'] + '\n' + 'First Name: ' + i['first_name'] + '\n' + 'Last Name: ' + i['last_name'] + '\n')
    
print('-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')

doc = db.student.find_one({'student_id': '1009'})

print('Student ID: ' + i['student_id'] + '\n' + 'First Name: ' + i['first_name'] + '\n' + 'Last Name: ' + i['last_name'] + '\n')
