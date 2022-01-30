from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Info




def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject , 
            message ,
            settings.EMAIL_HOST_USER,
            [email],
        )

       
    context = {
        'myinfo': myinfo
    }
    return render(request , 'contact/contact.html' , context)