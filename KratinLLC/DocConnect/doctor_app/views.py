from django.http import HttpResponse
from django.shortcuts import render
from doctor_app.models import doctor_login, doctor_profile
from patient_app.models import patient_login, patient_profile
from appointment_app.models import appointment
from django.core.mail import send_mail


def login_doctor(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = doctor_login.objects.filter(email=email)
        if data[0].password == password:
            request.session['doctor_login_id'] = data[0].id
            return render(request, 'doctor_home.html', {'login_data': data})
        else:
            return HttpResponse('Enter valid email or password')
    elif request.method == 'GET':
        return render(request, 'doctor_login.html')
    else:
        return HttpResponse("Unexpected Error")


def home_doctor(request):
    doctor_login_id = request.POST.get('doctor_login_id')
    data = doctor_profile.objects.filter(doctor_login_id=doctor_login_id)
    return render(request, 'doctor_profile.html', {'profile_data': data})


def appointment_doctor(request):
    doctor_login_id = request.session.get('doctor_login_id')
    data = appointment.objects.filter(doctor_id=doctor_login_id)
    patient_data = patient_profile.objects.filter(patient_login_id=data[0].patient_id)
    fetch_data = [{'id': data[0].id, 'patient_name': patient_data[0].name, 'date_time': data[0].date_time, 'status': data[0].appointment_status, 'patient_id': patient_data[0].patient_login_id}]
    return render(request, 'doc_appointment.html', {'appointment': fetch_data})


def approve(request):
    if "profile" in request.POST:
        patient_login_id = request.POST.get('patient_id')
        data = patient_profile.objects.filter(patient_login_id=patient_login_id)
        return render(request, 'patient_profile_view.html', {'profile_data': data})
    elif "approve" in request.POST:
        appointment_id = request.POST.get('appointment_id')
        status = request.POST.get('approval')
        appointment.objects.filter(id=appointment_id).update(appointment_status=status)
        a_data = appointment.objects.filter(id=appointment_id)
        p_data = patient_profile.objects.filter(patient_login_id=a_data[0].patient_id)
        e_data = patient_login.objects.filter(id=a_data[0].patient_id)
        d_data = doctor_profile.objects.filter(doctor_login_id=a_data[0].doctor_id)
        send_mail(
            'Appointment status',
            f'''Hii! {p_data[0].name},
                your appointment with {d_data[0].name} is {a_data[0].appointment_status}
                appointment date and time is {a_data[0].date_time}
                clinic address of doctor is {d_data[0].clinic_address}
            regards
            DocConnect Team''',
            'anirudha.djangotestmail@gmail.com',
            [e_data[0].email],
            fail_silently=False,
        )
        return render(request, 'doc_appointment.html')
