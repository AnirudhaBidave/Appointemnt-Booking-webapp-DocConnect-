from django.db import models


class appointment(models.Model):
    doctor_id = models.IntegerField()
    patient_id = models.IntegerField()
    date_time = models.DateTimeField()
    appointment_status = models.CharField(max_length=50)
