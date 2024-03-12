from django.shortcuts import render,redirect
from .forms import signup
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.conf import settings

User=settings


def userregister(req):
    if req.method=='POST':
        form=signup(req.POST or None)
        if form.is_valid():
            new_user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(req,f"Welcome {username},Your account has created successfully")
            new_user=authenticate(username=form.cleaned_data["email"],password=form.cleaned_data["password1"])
            login(req,new_user)
            return redirect('core:index')
            # email=form.cleaned_data.get('email')

        # print("Register")
    else:
        form=signup()

    return render(req,'core/newsignup.html',{'form':form})

def userlogin(req):
    if req.user.is_authenticated:
        print("Authenticated")
        # return redirect("core:index")
    if req.method=='POST':
        email=req.POST.get('email')
        password=req.POST.get('password')
        try:
            user=User.objects.get(email=email)
        except:
            messages.warning(req,f"Email doesn't exist")
        user=authenticate(req,email=email,password=password)
        if user is not None:
            login(req,user)
            messages.success(req,"You are logged in")
            return redirect("core:index")
        else:
            messages.warning(req,"User doesn't exist")
    return render(req,"core/newlogin.html")


def userlogout(req):
    logout(req)
    messages.success(req,"You are logged out")
    return redirect("userauths:userlogin")
# Create your views here.
