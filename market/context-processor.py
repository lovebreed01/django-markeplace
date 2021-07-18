from .views import user_message

def messages(request):
    from .models import Message
    if request.user.is_authenticated:
        messages = Message.objects.filter(chat_to=request.user).order_by('-time_stamp')
        return {'user_messages': messages} 
                
    else:
        return {'a':1,'b':2}
