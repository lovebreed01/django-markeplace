from django import forms
from django.forms import ModelForm, widgets
from .models import Item, Message,Images

class CreateItemForm(ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"placeholder":"What are you selling ?"}
        )
    )
   
    class Meta:
        model = Item
        exclude = ['seller','slug',]
        labels={
          "description" : "Describe" 
        }  
        widgets={
            'description': forms.Textarea(attrs={
                "placeholder":"Describe what you are selling clearly.."
            })
        }

        
class ItemEditForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['seller','slug']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields=['message',]
        labels={
            'message': ''
        }
        widgets={
            'message': forms.Textarea(attrs={
                "placeholder":"Your message here..",
                'id':'msg-input'
            })
        }
class ImagesUpload(ModelForm):
    files = forms.ClearableFileInput(attrs={'multiple':True})
    class Meta:
        model= Images
        fields=['files']

