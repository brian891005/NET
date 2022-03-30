from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from posts.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')

def index(request):
    return render(request, 'index.html')

def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

#登入
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')  #重新導向到首頁
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

# 登出
def log_out(request):
    logout(request)
    return redirect('/login') #重新導向到登入畫面

@login_required(login_url='/login')
def upload(request):
  
    if request.method == 'POST':
        form = Upload_Image_Form(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('/upload/success/')
    else:
        form = Upload_Image_Form()
    return render(request, 'upload.html', {'form' : form})
  
@login_required(login_url='/login')
def success(request):
    return HttpResponse('successfully uploaded')

@login_required(login_url='/login')
def list_all(request):
    images = Upload_Image.objects.all().order_by('id')
    context = {
        'images':images
    }
    return render(request,'listall.html',context)