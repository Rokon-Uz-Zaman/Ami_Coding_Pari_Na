from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate ,login 
from django.contrib.auth.views import LoginView


#create views for login
class UserLoginView(LoginView):
	template_name = 'signin.html'

#create views for sign up 
class UserSignUpView(CreateView):
	success_url =reverse_lazy('section2:khoj')
	template_name = 'signup.html'
	form_class = UserCreationForm
	def form_valid(self,form):
		to_return=super().form_valid(form)
		user=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password2"],)
		login(self.request,user)
		return to_return


