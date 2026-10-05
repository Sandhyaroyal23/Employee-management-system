from django.db import models
COURSE_CHOICE=[
    ('pfs','python full stack'),
    ('jfs','java full stack'),
    ('mern','mern full stack'),
    ('ai/ml','artificial intelligence machine learning')
]

class Student(models.Model):
    name=models.CharField(max_length=10)
    rollno=models.IntegerField()
    marks=models.IntegerField()
    address=models.TextField()
    course=models.CharField(max_length=100,choices=COURSE_CHOICE)
    
    def __str__(self):
        return self.name


