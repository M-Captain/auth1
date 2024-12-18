from django.shortcuts import render
from .forms import SignupForm ,LoginForm
from .models import Auth
from .auth import isuser

# Create your views here.
def user_login(request):
    form = LoginForm()
    p=""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            passw = isuser(data["email"])
            if not passw==False:
                if data["password"]==passw:
                    p="successful"
                else:
                    p="wrong credentials" 
            else:
                p="new member signup"
    return render(request,"login.html",{"form":form,"p":p})

def user_signup(request):
    form=SignupForm()
    p=""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if isuser(data["email"])==False:
                Auth.objects.create(**form.cleaned_data)
                p="successful"
            else:
                p="already member login"
    return render(request,"signup.html",{"form":form,"p":p})