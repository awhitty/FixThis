from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from html5 import forms as five_forms
from models import *

class SubmitForm(ModelForm):
	class Meta:
		model = Request
		exclude = ('timestamp', 'submitted_user', 'assigned_user', 'status')
	
	description = forms.CharField(
    	widget=forms.widgets.Textarea()
    )

	urgency = forms.IntegerField(
    	widget = five_forms.widgets.RangeInput(
            attrs = dict(
                min = '0',
                max = '10',
            ),
		)
	)

	tags = forms.MultipleChoiceField(
		choices=( (x.name, x.name) for x in Request.tags.most_common()),
		widget = forms.widgets.SelectMultiple(
			attrs = {
				'data-native-menu': 'false',
			}),
		)

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ('user')

class SlimUserCreationForm(UserCreationForm):
	username = forms.RegexField(
		label="Username", max_length=30,
		regex=r'^[\w.@+-]+$',
		error_messages={
			'invalid': "This value may contain only letters, numbers and "
					"@/./+/-/_ characters."},
		widget=forms.TextInput(
			attrs={'placeholder':'Username'}
		)
	)

	password1 = forms.CharField(
		label="Password",
        widget=forms.PasswordInput(
        	attrs={'placeholder':'Password'}
        )
    )

	password2 = forms.CharField(
		label="Password confirmation",
        widget=forms.PasswordInput(
        	attrs={'placeholder':'Password (again)'}
        )
	)

class SlimAuthenticationForm(AuthenticationForm):
	username = forms.CharField(
		label="Username", max_length=30,
		widget=forms.TextInput(
			attrs={'placeholder':'Username'}
		)
	)
	password = forms.CharField(
		label="Password",
        widget=forms.PasswordInput(
        	attrs={'placeholder':'Password'}
    	)
	)