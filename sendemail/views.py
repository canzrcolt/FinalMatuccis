from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def successView(request):
    return render(request, "success.html", {})

def indexView(request):
	return render(request, "index.html", {})

def successorderView(request):
	return render(request, "successorder.html", {})

def contactView(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		recipient_list = ['canzrcolt@gmail.com']
		message = " Email: " + message_email + "\n Name: " + message_name + "\n Message: " + message
		send_mail(message_name, message, message_email, recipient_list, fail_silently=False )
        
		

		

		return render(request, 'success.html', {'message_name': message_name})

	else:
		return render(request, "email.html", {})

def orderView(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_phone =  request.POST['message-phone']
		message_date = request.POST['message-date']
		message_time = request.POST['message-time']
		message_guests = request.POST['message-guests']
		message_address = request.POST['message-guests']
		
		message = request.POST['message']
		recipient_list = ['canzrcolt@gmail.com']
		message = " Email: " + message_email + "\n Name: " + message_name + "\n Phone Number: " + message_phone + "\n Date: " + message_date + "\n Time: " + message_time + "\n Number of Guests: " + message_guests + "\n Address: " + message_address + "\n Message: " +  message
		send_mail(message_name, message, message_email, recipient_list, fail_silently=False )
        
		

		

		return render(request, 'successorder.html', {'message_name': message_name})

	else:
		return render(request, "order.html", {})







