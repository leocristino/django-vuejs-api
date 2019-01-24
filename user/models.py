from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    age = models.IntegerField()
    password = models.CharField(max_length=250)
