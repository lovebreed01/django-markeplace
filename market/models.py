from django.db import models
from django.shortcuts import reverse
from datetime import datetime
from django.contrib.auth.models import  User
from django.utils.text import slugify
from user.models import State

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank = True)
    image = models.ImageField(upload_to='category_images', default='test.jpg')

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)
    

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    slug = models.SlugField(blank= True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(State, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug": self.slug})
    

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Item,self).save(*args,**kwargs)
        
    def get_first_img(self):
        return self.images_set.all()[0].files
    

    # def get_date(self):
        # time = datetime.now()
        # if self.created.day == time.day:
            # return f"{time.hour - self.created.hour} hours ago"
        # else :
            # if self.created.month == time.month:
                # return f"{time.day - self.created.day } days ago"
            # else:
                # if self.created.year == time.year:
                    # return f"{time.month - self.created.month} months ago"
        # return self.created
    def __str__(self):
        return f'{self.title}-{self.seller}'

    
class Images(models.Model):
    files = models.FileField(upload_to='item_images')
    item = models.ForeignKey(Item,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'image for {self.item}' 


class Message(models.Model):
    message = models.TextField()
    item = models.ForeignKey(Item,null=True,blank=True,on_delete=models.CASCADE)
    chat_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='chatto')
    chat_from = models.ForeignKey(User,on_delete=models.CASCADE,related_name='chatfrom')
    time_stamp= models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'message from {self.chat_from} to {self.chat_to} '


