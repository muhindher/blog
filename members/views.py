from re import template
#from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ProfileForm,UserUpdateForm
    

def registerPage(request):
	form=SignUpForm()
	if request.method=='POST':
		form=SignUpForm(request.POST)
		
		if form.is_valid():
			form.save()

			user=form.cleaned_data.get('username')
			messages.success(request,'Account Created for '+ user)
			return redirect('login')
	context={'form':form}
	return render(request,'members/register.html',context)

def loginPage(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None :
			login(request,user)
			return redirect('profile')
		else:
			messages.info(request,'Username Or Password is incorrect')
	context={}
	return render(request,'members/login.html',context)

@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('home')


# def profile(request):
# 	form=ProfileForm()
# 	if request.method=="POST":
# 		form=ProfileForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')
# 	context={'form':form}
# 	return render(request,'members/profile.html',context)


@login_required(login_url='login')
def profile(request):
	if request.method=='POST':
		p_form=ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if p_form.is_valid():
			p_form.save()
			messages.success(request,'Your Profile is Updated!')
			return redirect('index')

	else:
		p_form=ProfileForm()

	context={
	'p_form':p_form,
	}
	return render(request,'members/profile.html',context)

