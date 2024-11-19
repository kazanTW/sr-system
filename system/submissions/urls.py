from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_form, name='submit_form'),
    path('success/', views.success, name='success'),
    path('status/', views.case_status, name='case_status'),
]
