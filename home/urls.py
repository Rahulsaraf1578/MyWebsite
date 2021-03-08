from django.urls import path
from . import views
from django.core.mail import send_mail

urlpatterns = [
    path('', views.index, name="index"),
    path('contact',views.contact,name="contact")
]
