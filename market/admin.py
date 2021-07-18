from django.contrib import admin

from .models import Item,Category,Message,Images

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Images)