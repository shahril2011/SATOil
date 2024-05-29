from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    return render(request, 'sentiment_analysis/analyze.html')

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
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Redirect to a specified URL after login. Ensure this is a valid URL.
                return redirect("")  # Update this to the correct URL
            else:
                # Invalid login details provided
                print("Authentication failed: Invalid username or password")
        else:
            print("Form is invalid")
    
    context = {'loginform': form}
    return render(request, 'members/login.html', context=context)

def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return render(request, 'members/newPass.html', {'username': username})
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('reset_password')
    return render(request, 'members/resetPass.html')

def set_new_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            try:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                messages.success(request, 'Password reset successfully.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist.')
                return redirect('reset_password')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('set_new_password')
    return redirect('member_login')

def member_logout(request):
    
    auth.logout(request)
    return redirect('member_login')

@login_required(login_url='member_login')
def dashboard(request):
    user_name = request.user.username  # Assuming the username is used as the user's name
    return render(request, 'members/dashboard.html', {'user_name': user_name})

def sentiment_analysis(request):
    return render(request, 'sentiment_analysis/option.html')