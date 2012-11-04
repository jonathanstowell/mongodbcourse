
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db=connection.students
grades = db.grades


def find():

    print "find, reporting for duty"

    try:
        iter = grades.find({'type':'homework'}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]
    
    count = 0
    current_student_identifier = -1

    for item in iter:
        if (current_student_identifier != item['student_id']):
            grades.remove(item)
            count = count + 1

        current_student_identifier = item['student_id']

    print count
    print grades.count()

find()

