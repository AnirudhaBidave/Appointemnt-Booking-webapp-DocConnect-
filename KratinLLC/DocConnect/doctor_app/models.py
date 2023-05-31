from django.db import models


class doctor_login(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=10)


class doctor_profile(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)
    specialization = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    medical_licence_number = models.CharField(max_length=25)
    education = models.CharField(max_length=255)
    clinic_address = models.CharField(max_length=255)
    work_experience = models.IntegerField()
    doctor_login_id = models.IntegerField()
