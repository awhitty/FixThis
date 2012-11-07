from django import forms
from django.forms import ModelForm

from html5 import forms as five_forms
from models import Request

class SubmitForm(ModelForm):
	class Meta:
		model = Request
		exclude = ('timestamp')
	
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