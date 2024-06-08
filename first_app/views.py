from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
  return render(request,'home.html')



def signup(request):
  if not request.user.is_authenticated:
    if request.method=='POST':
      form=RegisterForm(request.POST)
      if form.is_valid():
        messages.success(request,'account create sucessfully')
        form.save()
    else:
      form=RegisterForm()
    return render(request,'signup.html',{'form':form})
  else:
    return redirect('profilepage')

def userlogin(request):
  if not request.user.is_authenticated:
    if request.method=="POST":
      form=AuthenticationForm(request=request,data=request.POST)
      if form.is_valid():
        name=form.cleaned_data['username']
        userpass=form.cleaned_data['password']
        user=authenticate(username=name,password=userpass)
        if user is not None:
          login(request,user)
          messages.success(request,'Logged In Successfully')
          return redirect('profilepage')
    else:
      form =AuthenticationForm()
    return render(request,'login.html',{'form':form})
  else:
    return redirect('profilepage')

def profile(request):
  if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, 'profile.html', {'form': form})
  else:
      return redirect('signup_page')

def user_logout(request):
  logout(request)
  messages.success(request,'Loggout In Successfully')
  return redirect('loginpage')


def pass_change(request):
  if request.user.is_authenticated:
    if request.method=="POST":
      form=PasswordChangeForm(user=request.user,data=request.POST)
      if form.is_valid():
        form.save()
        update_session_auth_hash(request,form.user)
        # pass update  korbe
        return redirect('profilepage')
    else:
      form=PasswordChangeForm(user=request.user)
    return render(request,'password_change.html',{'form':form})
  else:
    return redirect('loginpage')


def pass_change2(request):
  if request.user.is_authenticated:
    if request.method=="POST":
      form=SetPasswordForm(user=request.user,data=request.POST)
      if form.is_valid():
        form.save()
        update_session_auth_hash(request,form.user)
      # pass update  korbe
        return redirect('profilepage')
    else:
      form=SetPasswordForm(user=request.user)
    return render(request,'password_change.html',{'form':form})
  else:
    return redirect('loginpage')
  



