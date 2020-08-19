from django import forms

class ContactForm(forms.Form):
	from_email = forms.CharField(required=True)
	your_name = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea(attrs={"cols":33}), required=True)

class OrderForm(forms.Form):
	from_email = forms.CharField(required=True)
	your_name = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea(attrs={"cols":33}), required=True)
	party_size = forms.CharField(required=True)
	date = forms.CharField(required=False)
	image_link = forms.CharField(widget=forms.Textarea(attrs={"cols":20, "rows":3}), required=True)
	your_address = forms.CharField(required=True)
	your_phone = forms.CharField(required=True)
