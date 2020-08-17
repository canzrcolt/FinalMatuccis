from django import forms

class ContactForm(forms.Form):
	from_email = forms.CharField(required=True)
	your_name = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)

	
