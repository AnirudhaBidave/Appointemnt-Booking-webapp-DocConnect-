from django.urls import path
from patient_app import views
urlpatterns = [
    path('login_user', views.login_patient, name='user_login'),
    path('register_user', views.patient_registration, name='register_user'),
    path('profile_user', views.profile_patient, name='profile_user'),
    path('home_user', views.home_patient, name='home_user'),
    path('specialization', views.select_specialization, name='specialization'),
    path('doctor', views.select_doctor, name='doctor'),
]
