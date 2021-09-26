from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

## User
user_type = [
    ("Student", "Student"),
    ("Instructor", "Instructor")
]


class CustomUser(AbstractUser):
    address = models.CharField(max_length=50, blank=True, null=True, default=' ')
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=50, default='NE')
    zipcode = models.CharField(max_length=10, default='00000')
    email = models.EmailField(max_length=100, default=' ')
    cell_phone = models.CharField(max_length=50, default='(402)000-0000')
    date = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(choices=user_type, max_length=255)

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])


class Course(models.Model):
    courseName = models.CharField(max_length=30)
    courseType = models.CharField(max_length=30)
    courseCredit = models.IntegerField(max_length=30)
    courseDescription = models.CharField(max_length=30)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Grade(models.Model):
    grades = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D")
    ]

    gradeGiven = models.CharField(choices=grades, max_length=1)
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
