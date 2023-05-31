from django.db import models
# Create your models here.


class patient_login(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=10)


class patient_profile(models.Model):
    patient_login_id = models.IntegerField()
    name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    contact_number = models.IntegerField(max_length=15)
    allergies = models.CharField(max_length=255)
    medical_condition = models.CharField(max_length=255)
    previous_surgeries = models.CharField(max_length=255)
