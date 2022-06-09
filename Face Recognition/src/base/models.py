from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

    
class Student(models.Model):
    Lecturer=models.ForeignKey(User,on_delete=models.CASCADE)
    studentid=models.IntegerField()
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    ustatus=models.CharField(max_length=200)
    mobilenum=models.IntegerField()

    def __str__(self):
        return self.firstname
    

class Userinfo(models.Model):
    teacherinfo=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    mobilenum=models.IntegerField()
    address=models.CharField(max_length=200)




class Attendace(models.Model):
    teacheroperate=models.ForeignKey(User,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    attendancecreated=models.DateTimeField(auto_now_add=True)

    