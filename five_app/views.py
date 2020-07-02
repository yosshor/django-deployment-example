from django.shortcuts import render
from five_app.forms import UserForm, Userprofileinfoform
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def special(request):
    return HttpResponse('YOU ARE LOGED IN')

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def base(request):
    redundant = {'redundant': "<h1>we here because its redundant</h2>"}
    return render(request,'five_app/base.html',context=redundant)

def help(request):
    return render(request,'five_app/help.html')

def form(request):
    return render(request,'five_app/form.html')

def index(request):
    return render(request,'five_app/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user = UserForm(data = request.POST)
        profile = Userprofileinfoform(data = request.POST)

        if user.is_valid() and profile.is_valid():
            user = user.save()
            user.set_password(user.password)
            user.active=True
            user.staff=False
            user.admin=False
            user.save()
            messages.success(request, 'Account created successfully')

            profile = profile.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                print('we found that    ')
                profile.profile_image = request.FILES['profile_image']
            
            profile.save()
            registered = True

        else:
            print("something went wrong, user or profile is unvalid")
            print(user.errors,profile.errors)
   
    else:
        user = UserForm()
        profile = Userprofileinfoform()

    return render(request,'five_app/register.html',context={'user':user, 
                                                            'profile':profile,
                                                            'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request,username = username, password = password)
        print('after aunthenticate', user)

        if user:
        
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))        
            else:
                return HttpResponse('your account is not active')
        
        else:
            print("The username and password were incorrect.")
            print(f'username: {username} and password is {password}')
            return HttpResponse('unvalid login details')

    else:
        return render(request, 'five_app/login.html')
