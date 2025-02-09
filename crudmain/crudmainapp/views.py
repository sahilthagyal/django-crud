from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as django_login,logout as django_logout
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('Hello')
def insert(request):
    return render(request,'insert.html')
def InsertData(request):
    data = {
            }
    if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            contact = request.POST.get('contact')
            newuser = student.objects.create(first_name=fname, last_name=lname, email=email, contact=contact)
            data = {
            'first_name':fname,
            'last_name':lname,
            'email':email,
            'contact':contact
            }
    else:
        print('not a post request')
    print('hello')
    return redirect('showdata')

def showtable(request):
     return render(request,'show.html')
def showdata(request):
     alldata = student.objects.all()
     return render(request,'show.html',{'data':alldata})
def editdata(request,pk):
     data = student.objects.get(id=pk)
     return render(request,"edit.html",{"key":data})
def updatedata(request,pk):
    udata = student.objects.get(id=pk)
    udata.first_name=request.POST.get('fname')
    udata.last_name=request.POST.get('lname')
    udata.email=request.POST.get('email')
    udata.contact=request.POST.get('contact')
    udata.save()
    return redirect('showdata')
def deletedata(request,pk):
     ddata = student.objects.get(id=pk)
     ddata.delete()
     return redirect('showdata')
def user_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(uname,pass1)
        user = authenticate(request,username=uname,password=pass1)
        if user is not None:
            django_login(request,user)
            return redirect('insert')
        else:
             return HttpResponse('user not found')

    return render(request,'login.html')
def signuppage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        Email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2 :
             return HttpResponse('Password is not same ')
        else:
            userr = User.objects.create_user(username=uname, email=Email, password=pass1)
            return redirect('login')
    return render(request,'signup.html')
def logout(request):
    django_logout(request)
    return redirect(user_login)

     
