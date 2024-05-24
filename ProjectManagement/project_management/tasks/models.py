from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    item = models.CharField(max_length=255)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.CharField(max_length=255)
    autotimeline = models.DateField()


class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    interests = models.CharField(max_length=200)
    activitylog = models.CharField(max_length=200)
    interaction = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class StudyGroup(models.Model):
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)
    description = models.TextField()
    topic_category = models.CharField(max_length=50)

class CommunityForum(models.Model):
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)
    description = models.TextField()
    topic_category = models.CharField(max_length=50)

