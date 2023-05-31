from django.http import HttpResponse
from django.shortcuts import render, redirect
from patient_app.models import patient_login, patient_profile
from doctor_app.models import doctor_profile


def login_patient(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = patient_login.objects.filter(email=email)
        if len(data) == 0:
            return HttpResponse('Enter valid Email')
        elif data[0].password == password:
            request.session['patient_login_id'] = data[0].id
            pro_data = patient_profile.objects.filter(patient_login_id=data[0].id)
            if len(pro_data) == 0:
                return render(request, 'patient_profile.html', {'login_data': data})
            else:
                return render(request, 'patient_home.html', {'login_data': data})
        elif len(data) == 0:
            return HttpResponse('Enter valid Email')
        else:
            return HttpResponse('Enter valid Password')
    elif request.method == 'GET':
        return render(request, 'patient_login.html')
    else:
        return HttpResponse('Unexpected error')


def patient_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        while True:
            data = patient_login.objects.filter(email=email)
            if len(data) == 0:
                data = patient_login(username=username, email=email, password=password)
                data.save()
                return render(request, 'patient_login')
            else:
                return HttpResponse('Email id already register')
    elif request.method == 'GET':
        return render(request, 'register_patient.html')
    else:
        return HttpResponse('Unexpected error')


def profile_patient(request):
    patient_login_id = request.POST.get('patient_login_id')
    name = request.POST.get('name')
    dob = request.POST.get('dob')
    gender = request.POST.get('gender')
    contact_number = request.POST.get('contact_number')
    allergies = request.POST.get('allergies')
    medical_condition = request.POST.get('medical_condition')
    previous_surgeries = request.POST.get('previous_surgeries')
    data = patient_profile(patient_login_id=patient_login_id, name=name, dob=dob, gender=gender, contact_number=contact_number, allergies=allergies, medical_condition=medical_condition, previous_surgeries=previous_surgeries)
    data.save()
    return render(request, 'patient_home.html', {'profile_data': name})


def home_patient(request):
    patient_login_id = request.POST.get('patient_login_id')
    data = patient_profile.objects.filter(patient_login_id=patient_login_id)
    return render(request, 'patient_profile_view.html', {'profile_data': data})


def select_specialization(request):
    data = doctor_profile.objects.all().values('specialization').distinct()
    return render(request, 'specialization.html', {'profile_data': data})


def select_doctor(request):
    specialization = request.GET.get("specialization")
    data = doctor_profile.objects.filter(specialization=specialization)
    return render(request, 'appointment.html', {'profile_data': data})
