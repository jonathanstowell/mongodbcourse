
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db=connection.school
students = db.students


def find():

    print "find, reporting for duty"

    try:
        iter = students.find()

    except:
        print "Unexpected error:", sys.exc_info()[0]

    for student in iter:
        currentLowestHomework = None;
        for score in student['scores']:
            if (score["type"] == 'homework' and currentLowestHomework != None and currentLowestHomework["score"] > score["score"]):
                currentLowestHomework = score;
            elif (score["type"] == 'homework' and currentLowestHomework == None):
                currentLowestHomework = score;

        print "I will remove from student " + str(student["_id"]) + "lowest score: " + str(currentLowestHomework["score"]) + " with type: " + str(currentLowestHomework["type"]);
        students.update({ '_id' : student["_id"] }, { '$pull' : { 'scores' : { 'score' : currentLowestHomework["score"] } } });

find()

