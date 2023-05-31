from django.urls import path
from appointment_app import views

urlpatterns = [
    path('appointment', views.appointment_schedule, name='appointment'),
    path('schedule', views.schedule, name='schedule'),
]
