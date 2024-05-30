from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Django enquiry'
            body = {
                'name': form.cleaned_data['Name'],
                'email': form.cleaned_data['Email'],
                'message': form.cleaned_data['Message']
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, 'bobbyesaev@gmail.com', ['crayfishconfessionists@gmail.com'])
            except Exception as e:
                return HttpResponse(e)
            return redirect('/')
    return render(request, 'sendmail/contact.html', {'form': form})
