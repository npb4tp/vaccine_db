from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment, Patient
from .forms import PatientSignup
from django.shortcuts import redirect

def index(request):
    return render(request, 'landing.html')

def patient(request):
    appoint_list = Appointment.objects.all()
    if request.method == 'POST':
        form = PatientSignup(request.POST)
        fname = request.POST['patient_fname']
        lname = request.POST['patient_lname']
        dob = request.POST['patient_dob']
        allergies = request.POST['patient_allergies']
        street = request.POST['patient_street']
        city = request.POST['patient_city']
        state = request.POST['patient_state']
        zipc = request.POST['patient_zip']
        phone = request.POST['patient_phone']
        partially_vac = request.POST['patient_partially_vacc']
        patient = Patient.objects.create(patient_fname = fname, patient_lname = lname,patient_dob = dob,patient_allergies = allergies,patient_state = street,patient_zip = city,patient_city = state,patient_street = zipc,patient_phone = phone,patient_partially_vacc = partially_vac)
        patient.save()
        appoint = request.POST.get('app')
        APP = Appointment.objects.get(pk=appoint)
        APP.patient_id = patient
        APP.save()
        return redirect('/patient')
    else:
        form = PatientSignup()
    return render(request, 'patient.html', {'appoint_list': appoint_list, 'form':form})
