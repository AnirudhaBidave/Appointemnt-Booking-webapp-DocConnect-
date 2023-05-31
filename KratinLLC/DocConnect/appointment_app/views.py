from django.http import HttpResponse
# from patient_app.models import patient_login, patient_profile
# from doctor_app.models import doctor_login, doctor_profile
from appointment_app.models import appointment
from django.shortcuts import render


def appointment_schedule(request):
    doc_id = request.POST.get('doc_id')
    patient_login_id = request.session.get('patient_login_id')
    data = [{'doc_id': doc_id, 'patient_login_id': patient_login_id}]
    return render(request, 'schedule.html', {'appointment': data})


def schedule(request):
    doctor_id = request.POST.get('doc_id')
    patient_id = request.POST.get('patient_login_id')
    date_time = request.POST.get('date_time')
    appointment_status = 'pending'
    data = appointment(doctor_id=doctor_id, patient_id=patient_id, date_time=date_time, appointment_status=appointment_status)
    data.save()
    return HttpResponse('''Your appointment application has be submitted successfully
                            you will get an email after doctor approve the appointment
                                                Thank You''')
