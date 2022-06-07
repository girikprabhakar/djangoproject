from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    hours = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'),
                    ('CG', 'Calgary'),
                    ('MR', 'Montreal'),
                    ('VC', 'Vancouver')]
    name = models.CharField(max_length=200,null=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    interested_in = models.ManyToManyField(Topic)

    def __str__(self):
        return self.name

class Order(models.Model):
    CHOICES = [(0,0),(1,1)]
    course = models.ForeignKey(Course, related_name='orders', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='orders', on_delete=models.CASCADE)
    level = models.PositiveIntegerField(null=True)
    order_status = models.IntegerField(choices=CHOICES, default='1')
    order_date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return 'Order - ' + self.student.name + '_' + self.course.name

    def total_cost(self):
        return self.course.price * self.level