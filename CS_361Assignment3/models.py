from django.db import models


class Teacher(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    office_details=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    email=models.EmailField()


class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()


class Course(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=15)
    classroom=models.CharField(max_length=30)
    times=models.TimeField()
    teacher=models.ForeignKey(Teacher)
    students=models.ManyToManyField(Student)

