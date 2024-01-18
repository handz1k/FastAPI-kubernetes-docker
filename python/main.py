 
from fastapi import FastAPI
from mongoengine import (
    connect,
    disconnect,
    Document,
    StringField,
    ReferenceField,
    ListField,
    IntField
)
import json
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    connect("fast-api-database", host="mongo", port=27017)


@app.on_event("shutdown")
def shutdown_db_client():
    disconnect("fast-api-database")


# Helper functions to convert MongeEngine documents to json

def course_to_json(course):
    course = json.loads(course.to_json())
    course["students"] = list(map(lambda dbref: str(dbref["$oid"]), course["students"]))
    course["id"] = str(course["_id"]["$oid"])
    course.pop("_id")
    return course


def student_to_json(student):
    student = json.loads(student.to_json())
    student["id"] = str(student["_id"]["$oid"])
    student.pop("_id")
    return student

# Schema

class Student(Document):
    name = StringField(required=True)
    student_number = IntField()


class Course(Document):
    name = StringField(required=True)
    description = StringField()
    tags = ListField(StringField())
    students = ListField(ReferenceField(Student))



class CourseData(BaseModel):
    name: str
    description: str | None
    tags: list[str] | None
    students: list[str] | None


class StudentData(BaseModel):
    name: str
    student_number: int | None


# Student routes
# Complete the Student routes similarly as per the instructions provided in A+
@app.post('/students', status_code=201)
def create_student(student: StudentData):
    new_student = Student(**student.dict()).save()
    return {"message": "Student successfully created",
            "id": str(new_student.id)}

@app.get('/students/{student_id}', status_code = 200)
def get_student(student_id: str):
    student = Student.objects.get(id = student_id)
    return json.loads(student.to_json())

@app.put('/students/{student_id}', status_code = 200)
def update_student(student_id: str, student: StudentData):
    student_data = student.dict() 
    Student.objects(id=student_id).update(**student_data)
    return {"message": "Student successfully updated"}

@app.delete('/students/{student_id}', status_code = 200)
def delete_student(student_id: str):
    Student.objects.get(id = student_id).delete()
    return {"message": "Student successfully deleted"}


# Course routes
# Complete the Course routes similarly as per the instructions provided in A+

@app.post('/courses', status_code = 201)
def create_course(course: CourseData):
    new_course = Course(**course.dict()).save()
    return {"message": "Course successfully created",
            "id": str(new_course.id)}

@app.get('/courses', status_code = 200)
def get_courses(tag: str | None = None, studentName: str | None = None):
    if tag is None and studentName is None:
        courses = Course.objects()
        return json.loads(courses.to_json())
    elif tag is not None and studentName is None:
        courses = Course.objects.filter(tags = tag)
        return json.loads(courses.to_json())
    elif tag is None and studentName is not None:
        student_ids = [student.id for student in Student.objects(name=studentName)]
        courses = Course.objects.filter(students = student_ids)
        return json.loads(courses.to_json())
    else:
        student_ids = [s.id for s in Student.objects(name=studentName)]
        courses = Course.objects.filter(students = student_ids, tags = tag)
    return json.loads(courses.to_json())


@app.get('/courses/{course_id}', status_code = 200)
def get_course(course_id: str):
    course = Course.objects.get(id = course_id)
    return json.loads(course.to_json())

@app.put('/courses/{course_id}', status_code = 200)
def update_course(course_id: str, course: CourseData):
    course_data = course.dict()
    Course.objects(id=course_id).update(**course_data)
    return {"message": "Course successfully updated"}

@app.delete('/courses/{course_id}', status_code = 200)
def delete_course(course_id: str):
    Course.objects.get(id = course_id).delete()
    return {"message": "Course successfully deleted"}



    

