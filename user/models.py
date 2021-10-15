from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.enums import Choices
from django.db.models.manager import Manager


class State(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.name} state'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    phone_number = models.IntegerField( null=True,blank=True)
    profile_pic = models.FileField(upload_to = 'profile_pics', default='test.jpg',blank=True)
    location = models.ForeignKey(State,on_delete=models.CASCADE, null=True)

    def __str__(self):
    	return f'{self.user.username}  profile'

