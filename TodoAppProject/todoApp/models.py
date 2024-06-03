from django.db import models
from datetime import datetime
# Create your models here.

class Users(models.Model):

    # userId, First name, last name, phone, email-address

    UserId = models.IntegerField(primary_key=True, auto_created=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100)

    def __str__(self):
        return self.FirstName


# Properties of Task
# 1. Which User created that task, UserId, onetoone field
# 2. Unique id of Task.
# 3. Task Title
# 4. Task Description
# 5. Task Creation Date + Time
# 6. Task Status

STATUS = (
    ('1', 'Pending'),
    ('2', 'In Progress'),
    ('3', 'Completed'),
          )

class Task(models.Model):
    TaskId = models.IntegerField(primary_key=True, auto_created=True)
    TaskOfUserId = models.ForeignKey(Users, on_delete=models.CASCADE)
    TaskTitle = models.CharField(max_length=100)
    TaskDescription = models.CharField(max_length=300)
    TaskCreationTime = models.DateTimeField(default = datetime.now)
    TaskStatus = models.CharField(max_length=15, choices = STATUS, default="1")
    TaskUpdatedAt = models.DateTimeField(null=True)
    TaskCompletedAt = models.DateTimeField(null = True)

    

