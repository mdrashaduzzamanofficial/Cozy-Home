from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('dashboard/', views.landlord_dashboard, name='landlord_dashboard'),
    path('create/', views.create_property, name='create_property'),
    path('lease/<int:application_id>/', views.generate_lease, name='generate_lease'),
    path('payment/<int:property_id>/', views.make_payment, name='make_payment'),
    path('recommend/', views.recommend_properties, name='recommend_properties'),
]