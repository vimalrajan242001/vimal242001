from django.forms import ModelForm
from .models import leave_request
from django import forms
from django.contrib.auth import get_user_model



class leave_request_form(ModelForm):

	username=forms.CharField(label='uniqueID:',widget=forms.TextInput(attrs={'name':'username'}))
	email=forms.EmailField(label='Email address:',widget=forms.TextInput(attrs={'name':'email'}))
	start_date=forms.CharField(widget=forms.TextInput(attrs={'id':'datepicker','name':'start_date'}))
	end_date=forms.CharField(widget=forms.TextInput(attrs={'id':'datepicker1','name':'end_date'}))
	leaves=forms.IntegerField(label="number of days")

	class Meta:
		model = leave_request
		fields = [
			'username',
			'email',
			'course',
			'mentor',
			'leaves',
			'start_date',
			'end_date',
			'reason'
		]
