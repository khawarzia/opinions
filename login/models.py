from django.db import models
from django.contrib.auth.models import User

class infor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField(default=0)

    def __str__(self):
        return (self.user.username)