from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


from .forms import SignupForm
from .models import Profile
from .forms import ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.models import User
from .models import Profile

def redirect_users(request):
    if request.user.is_authenticated:
        return redirect('index')


def signup(request):
    redirect_users(request)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username,password=password)
            # my_user = form.instance
            # print(my_user)
            # profile.objects.create(user=my_user)
            # print(user)
            
            if user is not None:
                login(request,user)
                return redirect('complete-reg')
    else:
        form = SignupForm()
    return render(request, 'landing/signup.html',{'form':form})


def complete_reg(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=profile)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save(commit=False)
            p_form.instance.user = request.user
            p_form.save()
            u_form.save()
            print(p_form.cleaned_data)
            print(u_form.cleaned_data)
            return redirect('index')
    else:
        p_form = ProfileUpdateForm(instance=profile) 
        u_form = UserUpdateForm(instance=user)
    context = {
        'p_form': p_form,
        'u_form':u_form
    }
    return render(request,'landing/complete-reg.html',context)

@login_required   
def profile(request):
    profile = request.user.profile
    return render(request, 'market/profile.html',)