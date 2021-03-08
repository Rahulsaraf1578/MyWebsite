from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name,email,message,subject)

        send_mail(
            'message from ' + name,
            message+"\n"+email,
            email,
            ['rahulsaraf1578@gmail.com'],
            fail_silently=False
        )
        return render(request, 'index.html', {'name': name})
    else:
        return render(request, 'index.html', {})

