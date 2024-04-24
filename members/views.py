from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request, 'members/index.html')

def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect("member_login")

    context = {'registerform' : form}
    return render(request, 'members/register.html', context=context)

def member_login(request):

    form = LoginForm()

    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login(request, user)
                return redirect("dashboard")
            
    context = {'loginform' : form}
    return render(request, 'members/login.html', context=context)

def member_logout(request):
    
    auth.logout(request)
    return redirect("")

@login_required(login_url="member_login")
def dashboard(request):
    user_name = request.user.username  # Assuming the username is used as the user's name
    return render(request, 'members/dashboard.html', {'user_name': user_name})