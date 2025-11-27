from django.urls import path
from . import views

urlpatterns = [
    path('', views.message_inbox, name='message_inbox'),
    path('send/', views.send_message, name='send_message'),
]