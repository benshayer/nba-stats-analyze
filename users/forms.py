from django import forms
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

	def save(self,commit=True):
		user=super(UserRegisterForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()
	

	class Meta:
		model = User
		fields = ['username','email']	

	def save(self,commit=True):
		user=super(UserUpdateForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class ProfileUpdateForm(forms.ModelForm):
#	departments=[('Electronics','Electronics'),('Machine','Machine'),('Weapon','Weapon'),('Navigation','Navigation'),('Soldier','Soldier')]
#	department = forms.CharField(max_length=100,choices=departments, default='Soldier')

	class Meta:
		model = Profile
		fields = ['favorite_team']	
