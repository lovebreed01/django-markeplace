from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.enums import Choices
from django.db.models.manager import Manager
from cities_light.models import City
from cities_light.models import Region
from cities_light.models import Country
from smart_selects.db_fields import ChainedForeignKey




class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    phone_number = models.IntegerField( null=True,blank=True)
    profile_pic = models.FileField(upload_to = 'profile_pics', default='test.jpg',blank=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE, null=True)
    state = ChainedForeignKey(Region,chained_field='country', chained_model_field='country',null=True)

    def __str__(self):
    	return f'{self.user.username}  profile'

