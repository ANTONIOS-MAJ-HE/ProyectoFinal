from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def homes(request): 
    return render(request, 'Home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'Signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'Signup.html', {'form': form})
   
def homes(request): 
    return render(request, 'Home.html')
   
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'Home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'Login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'Login.html', {'form': form})
  
def profile(request): 
    return render(request, 'Profile.html')
   
def signout(request):
    logout(request)
    return redirect('/')