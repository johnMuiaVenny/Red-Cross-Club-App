import datetime
import json
import os

#import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render,redirect
from django.urls import reverse

from accounts.EmailBackEnd import EmailBackEnd
from accounts.models import CustomUser
from config import settings

# secret   6LeTfBYbAAAAAEAWPUEu_ANiR1mmXjhHc21uQZPj
# site  6LeTfBYbAAAAAF4tBZTgcmMA3Gtp9kNFgejdEFDk
def showDemoPage(request):
    return render(request,"demo.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:

        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("member_home"))
            
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def signup_member(request):
    return render(request,"signup_member_page.html")

def do_member_signup(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")


    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)
        user.save()
        messages.success(request,"Successfully Created Member")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"Failed to Create Member")
        return HttpResponseRedirect(reverse("show_login"))

# def do_member_signup(request):
# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		email = request.POST.get('email')
# 		password1 = request.POST.get('password1')
# 		password2 = request.POST.get('password2')
# 		if password1 == password2:
# 			if CustomUser.objects.filter(username=username).exists():
# 				messages.info(request, 'Username has been taken')
# 				return redirect('signup')
# 			elif CustomUser.objects.filter(email=email).exists():
# 				messages.info(request, 'Email already exists')
# 				return redirect('signup')
# 			else:
# 				user = CustomUser.objects.create_user(username=username, email=email, password=password1,user_type=2)
# 				user.save()
# 				messages.success(request, 'Congrats for signing up!')
# 				return redirect('signup')
# 		else:
# 			messages.info(request, 'password does not match')
# 			return redirect('signup')
# 	else:
# 		return render(request,'signup_member_page.html')
