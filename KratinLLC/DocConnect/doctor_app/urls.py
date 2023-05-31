from django.urls import path
from doctor_app import views

urlpatterns = [
    path('doctor_login', views.login_doctor, name='doctor_login'),
    path('doctor_home', views.home_doctor, name='doctor-home'),
    path('doctor_appointment', views.appointment_doctor, name='doctor_appointment'),
    path('approve', views.approve, name='approve'),
]
