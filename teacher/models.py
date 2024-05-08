from django.db import models
from django.contrib.auth.models import User
from student.models import Student
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="teacher/images/")
    subject =  models.ManyToManyField(Subject)
    available_time = models.ManyToManyField(AvailableTime)
    meet_link = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(Student, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Student : {self.reviewer.user.first_name} ; Teacher {self.teacher.user.first_name}"
