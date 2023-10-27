from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover, name='home'),
    path('c_emp', views.create_employee, name='c_emp'),
    path('success', views.success_view, name='success')
]