from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm	
from django.contrib import messages
from user.forms import UserRegisterForm

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account created {username}! You are Go for Login Now.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request,'register.html', {'form':form})


