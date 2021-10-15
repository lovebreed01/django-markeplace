from django.shortcuts import(get_object_or_404,
                            render,
                            redirect
                             )
from .models import Item,Category,Message, Images
from .forms import CreateItemForm,ItemEditForm,MessageForm,ImagesUpload
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages

#def is_seller(user):
#    item = Item.objects.get(args=[str(pk)])
 #   return user == item.sellers
 #   print(user == item.seller)


@login_required
def index(request):
    items = Item.objects.all().order_by('-created')
    categories = Category.objects.all()
    context ={
        'items':items,
        'categories':categories,
    }
    return render(request, 'market/index.html',context)

@login_required
def details(request,slug):
    item = Item.objects.get(slug = slug)
    images = Images.objects.filter(item = item)
    for img in images:
        print(img.files.url)
    related_items = Item.objects.filter(category = item.category).exclude(id=item.id)[:10]
    message = Message.objects.filter(chat_from = request.user)
    if request.method=='POST':
        messageform = MessageForm(request.POST)
        if messageform.is_valid():
            messageform.save(commit=False)
            messageform.instance.chat_from = request.user
            messageform.instance.chat_to = item.seller
            messageform.instance.item = item
            messageform.save()
            messages.success(request,'message sent successfully ! ')
    else:
        messageform = MessageForm() 
        
    context ={
        'messageform':messageform,
        'item':item,
        'related': related_items,
        'images':images,
    }
    return render(request,'market/details.html',context)

@login_required
def item_del(request,slug):
    item = get_object_or_404(Item, slug=slug)
    if request.method == 'POST':
        item.delete()
        item.message_set.all().delete()
        messages.success(request, 'Item and related messages successfully deleted ')
        return redirect("index")
    return render(request,'market/delete.html',{"item":item}) 

@login_required
def item_create(request):
    createform = CreateItemForm()
    imageform = ImagesUpload()
    if request.method == 'POST':
        createform = CreateItemForm(request.POST,request.FILES)
        imageform = ImagesUpload(request.POST,request.FILES)
        if createform.is_valid() and imageform.is_valid():
            createform.save(commit= False)
            imageform.save(commit=False)
            createform.instance.seller = request.user
            createform.save()
            print('item created')
            print(createform.instance)
            images = request.FILES.getlist('files')
            for i in images:
                image = Images.objects.create(files=i, item=createform.instance)
                print('image objects created')
                print(image)
            createform.instance.seller = request.user
            imageform.save()
            return redirect("index")
            messages.success(request, "Item successfully created")
        else:
            createform = CreateItemForm()
            imageform = ImagesUpload()

    return render(request, 'market/create.html',{'createform':createform,'imageform':imageform})
def item_edit(request,slug):
    item = Item.objects.get(slug=slug)
    form = ItemEditForm(instance=item)
    if request.method == 'POST':
        form = ItemEditForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save(commit= False)
            form.instance.seller = request.user
            form.save()
            return redirect("details", slug=item.slug)
            messages.success(request, "Item Successfully Edited")
        else:
            form = ItemEditForm(instance=item)
    return render(request, 'market/edit.html',{'form':form})
def category(request,slug):
    category = Category.objects.get(slug=slug)
    print(category.slug)
    items = Item.objects.filter(category = category).order_by('-created')
    context ={
        'items':items,
        'category':category,
    }
    return render(request, 'market/category.html',context)

def user_message(request):
    messages = Message.objects.filter(chat_to=request.user)
    
    return render(request,'market/message.html')