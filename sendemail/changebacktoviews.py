
# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, OrderForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            recipient_list = ['canzrcolt@gmail.com',]
            try:
                message = " Email: " + from_email + "\n Name: " + your_name + "\n Message: " + message
                send_mail(your_name, message, from_email, recipient_list, fail_silently=False )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def orderView(request):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name'] 
            from_email = form.cleaned_data['from_email']
            your_phone = form.cleaned_data['your_phone']
            your_address = form.cleaned_data['your_address']
            party_size = form.cleaned_data['party_size']
            date = form.cleaned_data['date']
            message = form.cleaned_data['message']
            image = form.cleaned_data['image']
            recipient_list = ['canzrcolt@gmail.com',]

          

            

            try:
                message = " Email: " + from_email + "\n Name: " + your_name + "\n Phone: " + your_phone + "\n Address: " + your_address + "\n Party Size: " + party_size + "\n Date: " + date + "\n Image: " + image
                send_mail(your_name, message, from_email, recipient_list, fail_silently=False )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "order.html", {'form': form})


def successView(request):
    return render(request, "success.html", {})

def indexView(request):
	return render(request, "index.html", {})

