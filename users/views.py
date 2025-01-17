from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('users:login')
    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('users:login')

@login_required
def profilepage(request):
    return render(request,'users/profile.html')
